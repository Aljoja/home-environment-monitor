import csv
from models import Measurement

def export_measurements_to_csv(
        measurements: list[Measurement], 
        filename: str,
        ):
    """
    Exports a list of Measurement objects to a CSV file.

    Args:
        measurements (list[Measurement]): A list of Measurement objects.
        filename (str): The name of the CSV file to write to.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'device_id', 'temperature_c', 'pressure_hpa', 'humidity_pct']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for measurement in measurements:
            writer.writerow({
                'timestamp': measurement.timestamp.isoformat(),
                'device_id': measurement.device_id,
                'temperature_c': measurement.temperature_c,
                'pressure_hpa': measurement.pressure_hpa,
                'humidity_pct': measurement.humidity_pct
            })

def append_measurement_to_csv(
        measurement: Measurement,
        filename: str
):
    """
    Appends a single Measurement object to an existing CSV file.

    Args:
        measurement (Measurement): The Measurement object to append.
        filename (str): The name of the CSV file to append to.
    """
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'device_id', 'temperature_c', 'pressure_hpa', 'humidity_pct']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:  # Check if the file is empty
            writer.writeheader()

        writer.writerow({
            'timestamp': measurement.timestamp.isoformat(),
            'device_id': measurement.device_id,
            'temperature_c': measurement.temperature_c,
            'pressure_hpa': measurement.pressure_hpa,
            'humidity_pct': measurement.humidity_pct
        })