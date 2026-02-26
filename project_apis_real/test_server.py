from prometheus_client import start_http_server, Gauge
import time

g = Gauge("test_metric", "Test Metric")

if __name__ == "__main__":
    start_http_server(9101)
    print("Server running on 9101")

    while True:
        g.set(5)
        time.sleep(5)