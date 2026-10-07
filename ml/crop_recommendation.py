import joblib
import numpy as np

# Load saved files
model = joblib.load("crop_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Input order:
# N, P, K, pH, Moisture, Temperature, Rainfall
input_data = np.array([[80, 40, 35, 6.8, 45, 28, 750]])

# Scale input
input_scaled = scaler.transform(input_data)

# Predict probabilities
probs = model.predict_proba(input_scaled)[0]

# Top 3 crops
top_3_idx = probs.argsort()[-3:][::-1]
top_3_crops = label_encoder.inverse_transform(top_3_idx)

print("Top 3 Recommended Crops:")
for crop in top_3_crops:
    print("-", crop)
