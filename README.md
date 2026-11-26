# Home Environment Monitor

A learning project for collecting environmental measurements. An ESP8266 running MicroPython reads a BME280 over I²C and sends readings as JSON over HTTP to a Python receiver on a PC. A desktop simulator can generate readings without hardware.

## Run the desktop simulator

From the repository root, run:

```powershell
python src/main.py
```

The simulator prints five readings and overwrites `measurements.csv`.

## Collect readings from the ESP8266

1. **Wire the BME280.** The ESP code uses GPIO5 (D1) for SCL, GPIO4 (D2) for SDA, and I²C address `0x76`.
2. **Configure the ESP.** Copy `esp/config_example.py` to `esp/config.py`. Set `SSID` and `PASSWORD` to your Wi-Fi credentials and `PC_IP` to the PC's LAN IP address. Git ignores `esp/config.py`.
3. **Copy the ESP files to the board.** Place `main.py`, `config.py`, `wifi_manager.py`, `http_client.py`, `sensor_reader.py`, and `bme280.py` from `esp/` in the board's filesystem root. Make sure `urequests` is available on the board.
4. **Start the receiver.** Run this from the repository root on the PC and leave it running.

   ```powershell
   python src/http_receiver.py
   ```

5. **Reset the ESP and check the output.** The board runs `main.py` on boot and posts readings to the PC on port `8000`. Each successful request receives HTTP `200` and adds a row to `esp_measurements.csv`. The receiver creates the file with a header on the first write.

Both CSV files contain a timestamp, device ID, temperature in °C, pressure in hPa, and relative humidity in %. The PC assigns the timestamp for ESP readings when it processes them.

## Run the desktop tests

With pytest installed, run this from the repository root:

```powershell
python -m pytest
```

The tests run without an ESP8266 or a running HTTP server.
