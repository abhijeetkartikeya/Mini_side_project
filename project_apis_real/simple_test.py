from prometheus_client import start_http_server, Gauge
import time

g = Gauge("my_metric", "Test metric")

if __name__ == "__main__":
    start_http_server(9200)
    print("Running on 9200")

    while True:
        g.set(123)
        time.sleep(2)