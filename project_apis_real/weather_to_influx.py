import requests
from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUX_URL = "http://localhost:8086"
TOKEN = "49oLD-HnmP2XyoLGkfen6itqjOU5Gy4j0wagxM5H_BkhkpkbJ-8h4CJ-uv8jKLmw60Y--kjDp4MKoA9nLYyvkQ=="
ORG = "weather-org"
BUCKET = "weather-bucket"

LAT = 28.7041
LON = 77.1025

end_date = datetime.utcnow().date()
start_date = end_date - timedelta(days=7)

url = f"https://archive-api.open-meteo.com/v1/archive?latitude={LAT}&longitude={LON}&start_date={start_date}&end_date={end_date}&hourly=cloud_cover,temperature_2m,wind_speed_10m,wind_gusts_10m,shortwave_radiation"

data = requests.get(url).json()["hourly"]

client = InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

for i in range(len(data["time"])):
    point = (
        Point("weather")
        .tag("location", f"{LAT},{LON}")
        .field("cloud_cover", float(data["cloud_cover"][i]))
        .field("temperature_2m", float(data["temperature_2m"][i]))
        .field("wind_speed_10m", float(data["wind_speed_10m"][i]))
        .field("wind_gusts_10m", float(data["wind_gusts_10m"][i]))
        .field("shortwave_radiation", float(data["shortwave_radiation"][i]))
        .time(data["time"][i], WritePrecision.NS)
    )
    write_api.write(bucket=BUCKET, org=ORG, record=point)

print("7-day historical data written.")