from src.models import Measurement
import pytest
import time

def test_measurement_str():
    measurement = Measurement(
        device_id="test_device",
        temperature_c=25.0,
        pressure_hpa=1013.25,
        humidity_pct=55.0,
    )
    expected_str = f"[{measurement.timestamp.strftime('%Y-%m-%d %H:%M:%S %z')}] test_device: 25.0 °C, 1013.25 hPa, 55.0% RH"
    assert str(measurement) == expected_str
    assert measurement.device_id == "test_device"
    assert measurement.temperature_c == 25.0
    assert measurement.pressure_hpa == 1013.25
    assert measurement.humidity_pct == 55.0

def test_empty_device_id():
    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="", 
        temperature_c=25.0,
        pressure_hpa=1013.25, 
        humidity_pct=55.0,
        )

def test_whitespace_device_id():
    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="   ", 
        temperature_c=25.0, 
        pressure_hpa=1013.25,
        humidity_pct=55.0,
        )

def test_humidity_limits():
    measurement_low = Measurement(
        device_id="test_device",
        temperature_c=25.0,
        pressure_hpa=1013.25,
        humidity_pct=0,
    )
    assert measurement_low.humidity_pct == 0.0

    measurement_high = Measurement(
        device_id="test_device",
        temperature_c=25.0,
        pressure_hpa=1013.25,
        humidity_pct=100.0,
    )
    assert measurement_high.humidity_pct == 100.0

def test_humidity_out_of_bounds():
    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="test_device", 
        temperature_c=25.0, 
        pressure_hpa=1013.25,
        humidity_pct=-1.0
    )

    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="test_device", 
        temperature_c=25.0, 
        pressure_hpa=1013.25,
        humidity_pct=101.0
    )

def test_temperature_limits():
    measurement_low = Measurement(
        device_id="test_device",
        temperature_c=-20.0,
        pressure_hpa=1013.25,
        humidity_pct=50.0
    )
    assert measurement_low.temperature_c == -20.0

    measurement_high = Measurement(
        device_id="test_device",
        temperature_c=60.0,
        pressure_hpa=1013.25,
        humidity_pct=50.0
    )
    assert measurement_high.temperature_c == 60.0

def test_temperature_out_of_bounds():
    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="test_device", 
        temperature_c=-21.0, 
        pressure_hpa=1013.25,
        humidity_pct=50.0
    )

    pytest.raises(
        ValueError, 
        Measurement, 
        device_id="test_device", 
        temperature_c=61.0, 
        pressure_hpa=1013.25,
        humidity_pct=50.0
    )

def test_timestamp_default_factory():
    measurement1 = Measurement(device_id="test_device")
    time.sleep(1)  # Ensure a different timestamp
    measurement2 = Measurement(device_id="test_device")
    assert measurement1.timestamp != measurement2.timestamp
    utc_offset1 = measurement1.timestamp.utcoffset()
    utc_offset2 = measurement2.timestamp.utcoffset()
    assert utc_offset1 is not None and utc_offset2 is not None

