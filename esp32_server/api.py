import socket
import time
import ujson

from configs import PinMap, pin_names, IOT_URL, CLICK_DURATION, API_HOST, API_PORT


# Helper function to control pins based on API request
def control_pin(pin_name, action):
    pin_number = pin_names.get(pin_name)

    if pin_number is not None:
        pin_map = PinMap.get_pin_map()
        pin = pin_map[pin_number]

        if action == "on":
            pin.value(1)  # Turn ON
            return f"{pin_name} turned ON"
        elif action == "off":
            pin.value(0)  # Turn OFF
            return f"{pin_name} turned OFF"
        elif action == "click":
            # Simulate a button click (press and release)
            pin.value(1)  # Button pressed (ON)
            time.sleep(CLICK_DURATION)  # Wait to simulate press duration
            pin.value(0)  # Button released (OFF)
            return f"{pin_name} clicked"
        else:
            return "Invalid action"
    else:
        return "Invalid pin"

def parse_request(request):
    try:
        # Split the request into lines
        request_lines = request.split('\r\n')
        if len(request_lines) < 1:
            return "Error: No request received"

        # Get the request method and URL
        method_and_url = request_lines[0].split(' ')
        method = method_and_url[0]
        url = method_and_url[1]  # This will give us the URL

        # Check for POST method
        if method != 'POST':
            return "Error: Only POST method is supported"

        # Check if the requested URL is correct
        if url != IOT_URL:
            return "Error: Invalid endpoint"

        # Initialize variables
        content_type = None
        content_length = 0

        # Read headers
        for line in request_lines:
            if line.startswith('Content-Type:'):
                content_type = line.split(': ')[1].strip()
            elif line.startswith('Content-Length:'):
                content_length = int(line.split(': ')[1].strip())

        # Check for JSON content
        if content_type == 'application/json' and content_length > 0:
            # Find where the headers end
            body_start_index = request.find('\r\n\r\n') + 4
            body = request[body_start_index:body_start_index + content_length]

            # Parse JSON
            json_data = ujson.loads(body)

            # Extract pin name and action from JSON data
            relay = json_data.get("pin")
            action = json_data.get("action")
            return control_pin(relay, action)
        else:
            return "Error: Unsupported content type or no content"
    except Exception as e:
        return f"Error processing request: {e}"


# Simple API server to control pins via HTTP
def start_api_server():
    addr = socket.getaddrinfo(API_HOST, API_PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print("API server listening on", addr)

    while True:
        client, addr = s.accept()
        print('Client connected from', addr)

        request = client.recv(1024).decode()

        # Parse the request for pin control
        response = parse_request(request)

        # Prepare HTTP response using a buffer
        response_buffer = bytearray()
        response_buffer.extend(b"HTTP/1.1 200 OK\r\n")
        response_buffer.extend(b"Content-Type: text/plain\r\n")
        response_buffer.extend(b"Connection: close\r\n\r\n")
        response_buffer.extend(response.encode('utf-8'))  # Convert the response to bytes

        # Send the entire response using the byte buffer
        client.sendall(response_buffer)
        client.close()

