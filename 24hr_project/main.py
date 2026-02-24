from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/weather")
def get_weather():
    df = pd.read_csv("weather_24h.csv")
    return df.to_dict(orient="records")