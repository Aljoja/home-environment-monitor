import urequests
import json
from config import PC_IP

URL = f"http://{PC_IP}:8000"

def send_measurement(measurement):
    """
    Sends a measurement to the server.
    """
    try:
        response = urequests.post(
            URL,
            data=json.dumps(measurement),
            headers={"Content-Type": "application/json"},
        )
    except OSError as e:
        print("Failed to send measurement:", e)
    else:
        try:
            http_status = response.status_code
            print("HTTP status code:", http_status)
        finally: # Ensure the response is closed to free up resources (finally block is always executed even if try block raises an exception)
            # print("Server replied:", response.text)
            response.close()

