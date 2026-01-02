import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

from src.models.dataset import load_training_data
from src.models.evaluation import evaluate_classification
from src.utils.logger import get_logger
from src.core.experiment_tracker import (
    start_experiment,
    log_params,
    log_metrics,
    log_model,
    end_experiment,
)

logger = get_logger()


def can_stratify(y) -> bool:
    """
    Stratification is only valid if every class has >= 2 samples.
    """
    counts = pd.Series(y).value_counts()
    return counts.min() >= 2


def main():
    # =========================
    # Load training data
    # =========================
    X, y = load_training_data(
        feature_path="data/processed/features.csv",
        raw_data_path="data/raw/sample_data.csv",
    )

    logger.info("Training data loaded")

    # =========================
    # Decide stratification safely
    # =========================
    stratify = y if can_stratify(y) else None

    if stratify is None:
        logger.warning(
            "Not enough samples per class for stratified split. "
            "Proceeding without stratification."
        )

    # =========================
    # Train / test split
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=stratify,
    )

    # =========================
    # Start MLflow experiment
    # =========================
    start_experiment("baseline-logistic-regression")

    log_params(
        {
            "model_type": "LogisticRegression",
            "max_iter": 1000,
            "test_size": 0.3,
            "stratified_split": stratify is not None,
        }
    )

    # =========================
    # Train model
    # =========================
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    logger.info("Model training completed")

    # =========================
    # Evaluate model
    # =========================
    preds = model.predict(X_test)
    metrics = evaluate_classification(y_test, preds)

    accuracy = metrics["accuracy"]

    logger.info(f"Model accuracy: {accuracy}")

    # =========================
    # Log metrics & model
    # =========================
    log_metrics(
        {
            "accuracy": accuracy,
        }
    )

    log_model(model)

    # =========================
    # Save model locally
    # =========================
    model_path = "models/baseline_model.joblib"
    joblib.dump(model, model_path)

    logger.info(f"Model saved to {model_path}")

    # =========================
    # End MLflow run
    # =========================
    end_experiment()


if __name__ == "__main__":
    main()

