import mlflow
from mlflow import sklearn


def start_experiment(experiment_name: str):
    mlflow.set_experiment(experiment_name)
    mlflow.start_run()


def log_params(params: dict):
    for k, v in params.items():
        mlflow.log_param(k, v)


def log_metrics(metrics: dict):
    for k, v in metrics.items():
        if v is not None:
            mlflow.log_metric(k, v)


def log_model(model, artifact_path: str = "model"):
    sklearn.log_model(model, artifact_path)


def end_experiment():
    mlflow.end_run()
