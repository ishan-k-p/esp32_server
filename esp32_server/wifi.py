import network
import time

from configs import WIFI_SSID, WIFI_PASSWORD


# Function to connect to Wi-Fi
def connect_wifi(display):
    ssid = WIFI_SSID
    password = WIFI_PASSWORD

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        display.custom_message("Connecting to WiFi...", 0, 16)
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi")
    display.start_continuous_message("wifi")
    print("Network Config:", station.ifconfig())
    display.custom_message(f"Network Config: {station.ifconfig()}", 0, 16)

