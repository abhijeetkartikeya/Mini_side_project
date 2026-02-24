import openmeteo_requests
import requests_cache
from retry_requests import retry
import time
from prometheus_client import start_http_server, Gauge

# Prometheus metrics
temperature = Gauge('temperature_2m', 'Temperature at 2m')
radiation = Gauge('shortwave_radiation', 'Solar radiation W/m2')

start_http_server(8000)

# Open-Meteo setup
cache_session = requests_cache.CachedSession('.cache', expire_after=0)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

params = {
    "latitude": 28.7041,
    "longitude": 77.1025,
    "current": ["temperature_2m", "shortwave_radiation"],
    "timezone": "Asia/Kolkata"
}

while True:
    responses = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    response = responses[0]
    current = response.Current()

    temp = current.Variables(0).Value()
    rad = current.Variables(1).Value()

    temperature.set(temp)
    radiation.set(rad)

    print("Updated:", temp, rad)

    time.sleep(15)