from collections import namedtuple
import machine

PinName = namedtuple('PinName', [
    'GPIO0', 'GPIO1', 'GPIO2', 'GPIO3', 'GPIO4',
    'GPIO5', 'GPIO12', 'GPIO13', 'GPIO14', 'GPIO15',
    'GPIO16', 'GPIO17', 'GPIO18', 'GPIO19', 'GPIO21',
    'GPIO22', 'GPIO23', 'GPIO25', 'GPIO26', 'GPIO27',
    'GPIO32', 'GPIO33', 'GPIO34', 'GPIO35', 'GPIO36',
    'GPIO37', 'GPIO38', 'GPIO39'
])

# Assign GPIO numbers
pins = PinName(
    GPIO0=0, GPIO1=1, GPIO2=2, GPIO3=3, GPIO4=4,
    GPIO5=5, GPIO12=12, GPIO13=13, GPIO14=14, GPIO15=15,
    GPIO16=16, GPIO17=17, GPIO18=18, GPIO19=19, GPIO21=21,
    GPIO22=22, GPIO23=23, GPIO25=25, GPIO26=26, GPIO27=27,
    GPIO32=32, GPIO33=33, GPIO34=34, GPIO35=35, GPIO36=36,
    GPIO37=37, GPIO38=38, GPIO39=39
)

# Map pin names to their corresponding GPIO numbers
pin_names = {
    "GPIO0": pins.GPIO0,
    "GPIO1": pins.GPIO1,
    "GPIO2": pins.GPIO2,
    "GPIO3": pins.GPIO3,
    "GPIO4": pins.GPIO4,
    "GPIO5": pins.GPIO5,
    "GPIO12": pins.GPIO12,
    "GPIO13": pins.GPIO13,
    "GPIO14": pins.GPIO14,
    "GPIO15": pins.GPIO15,
    "GPIO16": pins.GPIO16,
    "GPIO17": pins.GPIO17,
    "GPIO18": pins.GPIO18,
    "GPIO19": pins.GPIO19,
    "GPIO21": pins.GPIO21,
    "GPIO22": pins.GPIO22,
    "GPIO23": pins.GPIO23,
    "GPIO25": pins.GPIO25,
    "GPIO26": pins.GPIO26,
    "GPIO27": pins.GPIO27,
    "GPIO32": pins.GPIO32,
    "GPIO33": pins.GPIO33
    # GPIO34-39 are inputs only, so they are excluded
}

IOT_URL = "/devices/control"
CLICK_DURATION = 0.5
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
DDNS_TOKEN = "DuckDNS_TOKEN"
DDNS_DOMAIN = "DuckDNS_DOMAIN" #only the subdomain name
API_HOST = "0.0.0.0"
API_PORT = 1195
DNS_UPDATE_DURATION = 6000 # in seconds

class PinMap:
    @staticmethod
    def get_pin_map(pin_number=None):
        pin_map = {
            pins.GPIO0: machine.Pin(pins.GPIO0, machine.Pin.OUT),
            pins.GPIO1: machine.Pin(pins.GPIO1, machine.Pin.OUT),
            pins.GPIO2: machine.Pin(pins.GPIO2, machine.Pin.OUT),
            pins.GPIO3: machine.Pin(pins.GPIO3, machine.Pin.OUT),
            pins.GPIO4: machine.Pin(pins.GPIO4, machine.Pin.OUT),
            pins.GPIO5: machine.Pin(pins.GPIO5, machine.Pin.OUT),
            pins.GPIO12: machine.Pin(pins.GPIO12, machine.Pin.OUT),
            pins.GPIO13: machine.Pin(pins.GPIO13, machine.Pin.OUT),
            pins.GPIO14: machine.Pin(pins.GPIO14, machine.Pin.OUT),
            pins.GPIO15: machine.Pin(pins.GPIO15, machine.Pin.OUT),
            pins.GPIO16: machine.Pin(pins.GPIO16, machine.Pin.OUT),
            pins.GPIO17: machine.Pin(pins.GPIO17, machine.Pin.OUT),
            pins.GPIO18: machine.Pin(pins.GPIO18, machine.Pin.OUT),
            pins.GPIO19: machine.Pin(pins.GPIO19, machine.Pin.OUT),
            pins.GPIO21: machine.Pin(pins.GPIO21, machine.Pin.OUT),
            pins.GPIO22: machine.Pin(pins.GPIO22, machine.Pin.OUT),
            pins.GPIO23: machine.Pin(pins.GPIO23, machine.Pin.OUT),
            pins.GPIO25: machine.Pin(pins.GPIO25, machine.Pin.OUT),
            pins.GPIO26: machine.Pin(pins.GPIO26, machine.Pin.OUT),
            pins.GPIO27: machine.Pin(pins.GPIO27, machine.Pin.OUT),
            pins.GPIO32: machine.Pin(pins.GPIO32, machine.Pin.OUT),
            pins.GPIO33: machine.Pin(pins.GPIO33, machine.Pin.OUT)
            # GPIO34-39 are not included as they are input-only
        }

        if pin_number is None:
            return pin_map  # Return the complete map
        else:
            # Return the specific pin if it exists, otherwise return None
            return pin_map.get(pin_number, None)

