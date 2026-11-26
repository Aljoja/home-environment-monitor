import network
import time
from config import SSID, PASSWORD

def connect_wifi():
    # Disable access point and enable station mode
    ap = network.WLAN(network.WLAN.IF_AP)
    ap.active(False)

    # Enable station mode and connect to Wi-Fi
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            time.sleep(0.5)

    print("Connected:", wlan.ipconfig("addr4"))

def isconnected():
    wlan = network.WLAN(network.WLAN.IF_STA)
    return wlan.isconnected()