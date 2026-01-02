from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

from src.models.dataset import load_training_data
from src.utils.logger import get_logger

logger = get_logger()


def main():
    X, y = load_training_data(
        feature_path="data/processed/features.csv",
        raw_data_path="data/raw/sample_data.csv",
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    logger.info(f"Model trained successfully")
    logger.info(f"Accuracy: {acc:.4f}")
    logger.info("Classification Report:")
    logger.info("\n" + classification_report(y_test, preds))

    joblib.dump(model, "models/baseline_model.joblib")
    logger.info("Model saved to models/baseline_model.joblib")


if __name__ == "__main__":
    main()
