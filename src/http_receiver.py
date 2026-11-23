"""
RESPONSABILITY:
receive JSON from the ESP and convert that incoming 
data into your existing Measurement domain model.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MeasurementHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        measurement = json.loads(body)

        print("Received measurement:")
        print(measurement)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


server = HTTPServer(("0.0.0.0", 8000), MeasurementHandler)

print("Listening on port 8000...")
server.serve_forever()