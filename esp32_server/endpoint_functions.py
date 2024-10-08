from esp32_server.auth import register_user, edit_user, delete_user, login_user
from esp32_server.configs import USER_OPERATIONS, LOGIN, IOT_URL, pin_names, PinMap, CLICK_DURATION
import time


# Helper function to control pins based on API request
def control_pin(pin_name, action):
    pin_number = pin_names.get(pin_name)

    if pin_number is not None:
        pin_map = PinMap.get_pin_map()
        pin = pin_map[pin_number]

        if action == "on":
            pin.value(1)  # Turn ON
            return True, f"{pin_name} turned ON"
        elif action == "off":
            pin.value(0)  # Turn OFF
            return True, f"{pin_name} turned OFF"
        elif action == "click":
            # Simulate a button click (press and release)
            pin.value(1)  # Button pressed (ON)
            time.sleep(CLICK_DURATION)  # Wait 100ms to simulate press duration
            pin.value(0)  # Button released (OFF)
            return True, f"{pin_name} clicked"
        else:
            return False, "Invalid action"
    else:
        return False, "Invalid pin"

def do_user_operations(http_method, json_body):
    try:
        username = json_body.get("username")
        password = json_body.get("password")
        if http_method == 'POST':
            return register_user(username, password)
        elif http_method == 'PUT':
            return edit_user(username, password)
        elif http_method == 'DELETE':
            return delete_user(username)
    except Exception as e:
        return f"Error processing request: {e}"

def login(http_method, json_body):
    try:
        username = json_body.get("username")
        password = json_body.get("password")
        if http_method == "POST":
            return login_user(username, password)
        else:
            return False, "Error: Only POST method is supported"
    except Exception as e:
        return f"Error processing request: {e}"

def trigger_pins(http_method, json_body): # authenticate before letting through
    try:
        relay = json_body.get("pin")
        action = json_body.get("action")
        if http_method == "POST":
            return control_pin(relay, action)
        else:
            return False, "Error: Only POST method is supported"
    except Exception as e:
        return f"Error processing request: {e}"

def direct_requests(URL, json_body, http_method):
    if URL == USER_OPERATIONS:
        do_user_operations(http_method, json_body)
    elif URL == LOGIN:
        login(http_method, json_body)
    elif URL == IOT_URL:
        trigger_pins(http_method, json_body)