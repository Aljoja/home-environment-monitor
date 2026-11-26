"""
RESPONSABILITY:
receive JSON from the ESP and convert that incoming 
data into your existing Measurement domain model.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from exports import append_measurement_to_csv
from models import Measurement
import json

def measurement_from_payload(payload: dict) -> Measurement:
    """
    Converts a JSON payload from the ESP into a Measurement object.

    Args:
        payload (dict): The JSON payload received from the ESP.

    Returns:
        Measurement: A Measurement object representing the received data.
    """
    temperature = payload['temperature']
    pressure = payload['pressure']
    humidity = payload['humidity']

    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number")

    if not isinstance(pressure, (int, float)):
        raise ValueError("Pressure must be a number")

    if not isinstance(humidity, (int, float)):
        raise ValueError("Humidity must be a number")

    return Measurement(
        device_id='esp8266_1',  # You can modify this to extract from payload if needed
        temperature_c=temperature,
        pressure_hpa=pressure,
        humidity_pct=humidity,
    )
class MeasurementHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handle POST requests to receive measurement data from the ESP.
        The incoming data is expected to be in JSON format and will be 
        printed to the console.
        """

        # Read the content length and body of the request
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        try: # Parse the incoming JSON payload
            payload = json.loads(body)
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON in request body")
            return

        if not isinstance(payload, dict):
            self.send_error(400, "Payload must be a JSON object")
            return

        try: # Convert the payload into a Measurement object
            measurement = measurement_from_payload(payload)
        except KeyError as e:
            print(f"Error: Missing key in payload - {e}")
            self.send_error(400, "Missing required measurement field")
            return
        except ValueError as e:
            print(f"Error: Invalid value in payload - {e}")
            self.send_error(400, str(e))
            return

        # Append to csv
        append_measurement_to_csv(measurement, "esp_measurements.csv")
        print("Received measurement:")
        print(measurement)

        # Send a 200 OK response back to the ESP
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


if __name__ == "__main__":

    # Start the HTTP server
    server = HTTPServer(("0.0.0.0", 8000), MeasurementHandler)

    print("Listening on port 8000...")
    # Keep the server running indefinitely to handle incoming requests
    server.serve_forever()