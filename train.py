import mlflow
import random

mlflow.set_experiment("mcp_forecasting")

with mlflow.start_run():
    lr = 0.01
    rmse = random.uniform(10, 20)

    mlflow.log_param("learning_rate", lr)
    mlflow.log_metric("rmse", rmse)

print("Run logged successfully.")