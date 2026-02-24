import requests
import pandas as pd

url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=22&longitude=79"
    "&hourly=temperature_2m,wind_speed_10m,shortwave_radiation"
    "&past_days=1"
    "&timezone=Asia%2FTokyo"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "wind": data["hourly"]["wind_speed_10m"],
    "solar": data["hourly"]["shortwave_radiation"]
})

df.to_csv("weather_24h.csv", index=False)

print("CSV created successfully.")