import csv
import pytest
from datetime import datetime
from datetime import timezone

from src.models import Measurement
from src.exports import (
    export_measurements_to_csv, 
    append_measurement_to_csv,
)


def test_export_measurements_to_csv(tmp_path):
    csv_path = tmp_path / "measurements.csv"
    measurements = [
        Measurement(
            device_id="device_1", 
            timestamp=datetime(2024, 6, 1, 12, 0, tzinfo=timezone.utc),
            temperature_c=21.123456, 
            pressure_hpa=1013.25,
            humidity_pct=47.654321
            ),
        Measurement(
            device_id="device_2", 
            timestamp=datetime(2024, 6, 1, 12, 0, tzinfo=timezone.utc),
            temperature_c=25.0, 
            pressure_hpa=1015.0,
            humidity_pct=50.0
            ),
    ]
    export_measurements_to_csv(measurements, csv_path)

    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert reader.fieldnames == ['timestamp', 'device_id', 'temperature_c', 'pressure_hpa', 'humidity_pct']
    assert len(rows) == 2
    assert rows[0]['device_id'] == "device_1"
    assert rows[0]["timestamp"] == "2024-06-01T12:00:00+00:00"
    assert float(rows[0]['temperature_c']) == 21.123456
    assert float(rows[0]['pressure_hpa']) == 1013.25
    assert float(rows[0]['humidity_pct']) == 47.654321
    assert rows[1]['device_id'] == "device_2"
    assert rows[1]['timestamp'] == "2024-06-01T12:00:00+00:00"
    assert float(rows[1]['temperature_c']) == 25.0
    assert float(rows[1]['pressure_hpa']) == 1015.0
    assert float(rows[1]['humidity_pct']) == 50.0

def test_append_measurement_to_csv(tmp_path):

    csv_path = tmp_path / "esp_measurements.csv"
    measurement1 = Measurement(
        device_id="device_1", 
        timestamp=datetime(2024, 6, 1, 12, 0, tzinfo=timezone.utc),
        temperature_c=21.123456, 
        pressure_hpa=1013.25,
        humidity_pct=47.654321
    )
    measurement2 = Measurement(
        device_id="device_2", 
        timestamp=datetime(2024, 6, 1, 12, 5, tzinfo=timezone.utc),
        temperature_c=25.0, 
        pressure_hpa=1015.0,
        humidity_pct=50.0
    )
    append_measurement_to_csv(measurement1, csv_path)
    append_measurement_to_csv(measurement2, csv_path)

    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    assert reader.fieldnames == ['timestamp', 'device_id', 'temperature_c', 'pressure_hpa', 'humidity_pct']
    assert len(rows) == 2
    assert rows[0]['device_id'] == "device_1"
    assert rows[0]["timestamp"] == "2024-06-01T12:00:00+00:00"
    assert float(rows[0]['temperature_c']) == 21.123456
    assert float(rows[0]['pressure_hpa']) == 1013.25
    assert float(rows[0]['humidity_pct']) == 47.654321
    assert rows[1]['device_id'] == "device_2"
    assert rows[1]['timestamp'] == "2024-06-01T12:05:00+00:00"
    assert float(rows[1]['temperature_c']) == 25.0
    assert float(rows[1]['pressure_hpa']) == 1015.0
    assert float(rows[1]['humidity_pct']) == 50.0