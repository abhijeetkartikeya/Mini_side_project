from prometheus_client import Gauge, start_http_server
import requests
import time
import threading
import os

print("Weather MCP server started...")

# ---- CONFIG ----
API_KEY = "cb7e0323de55706b9de9ed05e69ebf63"

CITY = "Delhi"
INTERVAL = 60  # seconds

# ---- PROMETHEUS METRIC ----
temperature = Gauge(
    "india_temperature_celsius",
    "Current temperature in Delhi"
)

# ---- OPENWEATHER URL ----
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


def update_temperature():
    while True:
        try:
            response = requests.get(URL, timeout=10)

            print("Status Code:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                print("Temperature:", temp)
                temperature.set(temp)
            else:
                print("API Error Response:", response.text)

        except Exception as e:
            print("Exception:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8000)
    print("Prometheus metrics server running on port 8000")

    # Start background update thread
    thread = threading.Thread(target=update_temperature)
    thread.daemon = True
    thread.start()

    # Keep main thread alive
    while True:
        time.sleep(1)