from machine import Pin, I2C
import bme280

i2c = I2C(
    scl=Pin(5),   # D1
    sda=Pin(4),   # D2
)

bme_sensor = bme280.BME280( # Initialize the BME280 sensor with the I2C interface
    i2c=i2c,            # no need to reinitialize the I2C interface, just pass it to the BME280 constructor
    address=0x76,
)


def read_environment():
    temperature, pressure, humidity = bme_sensor.values
    return {
        "temperature": temperature,
        "pressure": pressure / 100,
        "humidity": humidity,
    }