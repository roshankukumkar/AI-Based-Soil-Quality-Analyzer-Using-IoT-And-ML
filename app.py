import os
import pickle
import numpy as np
import serial
import time
import threading

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)

# ---------------- MODEL ----------------
model = pickle.load(open(os.path.join(BASE_DIR, "ml", "crop_model.pkl"), "rb"))
label_encoder = pickle.load(open(os.path.join(BASE_DIR, "ml", "label_encoder.pkl"), "rb"))

# ---------------- ARDUINO ----------------
try:
    arduino = serial.Serial("COM6", 9600, timeout=2)
    time.sleep(2)
    arduino.reset_input_buffer()
    print("✅ Arduino Connected")
except Exception as e:
    print("❌ Arduino Not Connected:", e)
    arduino = None

# ---------------- SENSOR DATA STORAGE ----------------
last_values = {
    "temperature": 0,
    "humidity": 0,
    "soil_moisture": 0
}

# ---------------- BACKGROUND READER THREAD ----------------
def read_sensor_loop():
    global last_values, arduino

    while True:
        try:
            if arduino is None:
                time.sleep(2)
                continue

            line = arduino.readline().decode("utf-8", errors="ignore").strip()

            if ":" not in line:
                continue

            print("RAW:", line)

            values = {}

            for part in line.split(","):
                if ":" in part:
                    k, v = part.split(":")
                    try:
                        values[k.strip()] = float(v.strip())
                    except:
                        pass

            if "T" in values:
                last_values["temperature"] = values["T"]

            if "H" in values:
                last_values["humidity"] = values["H"]

            if "M" in values:
                last_values["soil_moisture"] = values["M"]

        except Exception as e:
            print("Sensor read error:", e)

        time.sleep(1)

# start thread
threading.Thread(target=read_sensor_loop, daemon=True).start()

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_sensor_data")
def get_sensor_data():
    return jsonify(last_values)

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])

    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    temperature = last_values["temperature"]
    humidity = last_values["humidity"]
    soil_moisture = last_values["soil_moisture"]

    features = np.array([[
        N, P, K,
        temperature,
        humidity,
        soil_moisture,
        ph,
        rainfall
    ]])

    probs = model.predict_proba(features)[0]

    idx = np.argmax(probs)
    crop = label_encoder.inverse_transform([idx])[0]
    confidence = probs[idx] * 100

    return render_template(
        "result.html",
        crop=crop,
        confidence=round(confidence, 2),

        N=N, P=P, K=K,
        ph=ph,
        rainfall=rainfall,
        temperature=temperature,
        humidity=humidity,
        soil_moisture=soil_moisture
    )

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)