from prometheus_client import start_http_server, Gauge
import requests
import time

temperature = Gauge('india_temperature_celsius', 'Temperature in Celsius')
wind_speed = Gauge('india_wind_speed_kmh', 'Wind Speed in km/h')
solar_radiation = Gauge('india_solar_radiation_w_m2', 'Solar Radiation W/m2')

LAT = 25.5
LON = 75.25

def fetch_weather():
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LAT}&longitude={LON}"
        f"&hourly=temperature_2m,windspeed_10m,shortwave_radiation"
        f"&past_days=1"
    )

    response = requests.get(url)
    data = response.json()

    temps = data["hourly"]["temperature_2m"]
    winds = data["hourly"]["windspeed_10m"]
    solar = data["hourly"]["shortwave_radiation"]

    # latest hour
    temperature.set(temps[-1])
    wind_speed.set(winds[-1])
    solar_radiation.set(solar[-1])

    print("Last 24h pulled. Latest values set.")

if __name__ == "__main__":
    start_http_server(8000)
    print("Exporter running on port 8000")

    while True:
        try:
            fetch_weather()
        except Exception as e:
            print("Error:", e)

        time.sleep(3600)   # hourly pull