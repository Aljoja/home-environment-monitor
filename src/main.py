from time import sleep

from simulator import Simulator
from exports import export_measurements_to_csv


def main():
    simulator = Simulator(
        temperature_c=22.0,
        humidity_pct=50.0,
        device_id="living_room_001"
    )

    measurements = []

    for _ in range(5):
        
        measurement = simulator.generate_measurement()
        measurements.append(measurement)
        print(measurement)
        sleep(2)  # Simulate a delay between measurements

    return measurements



if __name__ == "__main__":
    measurements = main()
    export_measurements_to_csv(
        measurements, 
        "measurements.csv",
        )