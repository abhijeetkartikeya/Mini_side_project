from flask import Flask
from prometheus_client import Gauge, generate_latest
import requests
import time
import threading
from flask import Response
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

india_temperature = Gauge(
    'india_temperature_celsius',
    'Current temperature in Delhi'
)

API_KEY = "cb7e0323de55706b9de9ed05e69ebf63"
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},IN&appid={API_KEY}&units=metric"


def fetch_temperature():
    while True:
        try:
            response = requests.get(URL)
            data = response.json()
            temp = data['main']['temp']
            india_temperature.set(temp)
            print("Updated temperature:", temp)
        except Exception as e:
            print("Error:", e)

        time.sleep(60)


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    t = threading.Thread(target=fetch_temperature)
    t.daemon = True
    t.start()
    app.run(host="0.0.0.0", port=8000)