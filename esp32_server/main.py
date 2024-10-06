import _thread
import time
import wifi
import duckdns
import api

# Main function to start tasks on both cores
def main():
    wifi.connect_wifi()  # Connect to Wi-Fi

    # Start DuckDNS updater on Core 0
    _thread.start_new_thread(duckdns.duckdns_updater_task, ())

    # Start API server for GPIO control on Core 1
    _thread.start_new_thread(api.start_api_server, ())

# Entry point of the script
if __name__ == "__main__":
    main()

# Keep the main thread alive
while True:
    time.sleep(1)
