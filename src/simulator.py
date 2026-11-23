import random
from models import Measurement

class Simulator:

    def __init__(
            self, 
            temperature_c=21.5, 
            humidity_pct=47.0,
            device_id=None,
            ):
        self.temperature_c = temperature_c
        self.humidity_pct = humidity_pct
        self.device_id = device_id

    def generate_measurement(self):
        
        self.temperature_c += random.uniform(-0.1, 0.1)
        self.humidity_pct += random.uniform(-0.3, 0.3)
        if self.humidity_pct < 0:
            self.humidity_pct = 0
        elif self.humidity_pct > 100:
            self.humidity_pct = 100 
        if self.temperature_c < -20:
            self.temperature_c = -20
        elif self.temperature_c > 60:
            self.temperature_c = 60
        
        return Measurement(
            device_id=self.device_id,
            temperature_c=self.temperature_c,
            humidity_pct=self.humidity_pct
        )