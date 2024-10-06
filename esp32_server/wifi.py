import network
import time

from configs import WIFI_SSID, WIFI_PASSWORD


# Function to connect to Wi-Fi
def connect_wifi():
    ssid = WIFI_SSID
    password = WIFI_PASSWORD

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi")
    print("Network Config:", station.ifconfig())
