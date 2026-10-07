import serial
import time

arduino = serial.Serial(
    "COM6",
    9600,
    timeout=5
)

time.sleep(5)

print("Connected to Arduino")

while True:

    if arduino.in_waiting > 0:

        data = arduino.readline().decode(
            errors="ignore"
        ).strip()

        print(data)