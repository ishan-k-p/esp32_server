import urequests
import time

from configs import DDNS_TOKEN, DDNS_DOMAIN, DNS_UPDATE_DURATION

# DuckDNS settings
duckdns_token = DDNS_TOKEN
duckdns_domain = DDNS_DOMAIN

# DuckDNS Updater task to run on Core 0
def duckdns_updater_task():
    while True:
        url = f"https://www.duckdns.org/update?domains={duckdns_domain}&token={duckdns_token}&ip="

        try:
            response = urequests.get(url)
            if response.status_code == 200:
                print("DuckDNS updated successfully.")
            else:
                print("Failed to update DuckDNS:", response.status_code)
        except Exception as e:
            print("Error updating DuckDNS:", e)

        time.sleep(DNS_UPDATE_DURATION)  # Update every 10 minutes
