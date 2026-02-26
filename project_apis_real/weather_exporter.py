from prometheus_client import start_http_server, Gauge
import requests
import time

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=22.25,13.32,16.04&longitude=72.74,78.66,75.05&hourly=cloud_cover&minutely_15=temperature_2m,wind_speed_10m,shortwave_radiation,wind_gusts_10m&timezone=auto"

g_cloud = Gauge("weather_cloud_cover", "Cloud Cover", ["location"])
g_temp = Gauge("weather_temperature_2m", "Temperature", ["location"])

def collect():
    r = requests.get(API_URL)
    data = r.json()

    for loc in data:
        location = f"{loc['latitude']},{loc['longitude']}"

        g_cloud.labels(location).set(loc["hourly"]["cloud_cover"][-1])
        g_temp.labels(location).set(loc["minutely_15"]["temperature_2m"][-1])

if __name__ == "__main__":
    start_http_server(9201)
    print("Weather exporter running on 9201")

    while True:
        try:
            collect()
        except Exception as e:
            print("ERROR:", e)
        time.sleep(30)