from src.http_receiver import measurement_from_payload

def test_measurement_from_payload():
    payload = {
        "temperature": 23.1,
        "pressure": 1020.42,
        "humidity": 58.5
    }

    measurement = measurement_from_payload(payload)

    assert measurement.device_id == 'esp8266_1'
    assert measurement.timestamp.utcoffset() is not None  # Check that timestamp has timezone info
    assert measurement.temperature_c == 23.1
    assert measurement.pressure_hpa == 1020.42
    assert measurement.humidity_pct == 58.5