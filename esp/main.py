"""
commands:
mpremote connect COM3 fs cp sensor_reader.py :sensor_reader.py
mpremote connect COM3 fs cp http_client.py :http_client.py
mpremote connect COM3 fs cp wifi_manager.py :wifi_manager.py
python http_receiver.py
mpremote connect COM3 run main.py
"""
import time
from wifi_manager import connect_wifi, isconnected
from sensor_reader import read_environment
from http_client import send_measurement

# Connect to Wi-Fi
connect_wifi()

counter = 0
while True:
    counter += 1
    print(f"Reading {counter}...")
    print("Wi-Fi connected:", isconnected())

    # Read sensor data
    measurement = read_environment()

    print("Sending:")
    print(measurement)

    # Send the measurement to the server
    send_measurement(measurement)

    time.sleep(10)  # Wait for 10 seconds before the next reading