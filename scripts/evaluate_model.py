import joblib
from sklearn.linear_model import LogisticRegression

from src.models.dataset import load_training_data
from src.models.evaluation import evaluate_classification
from src.models.cross_validation import cross_validate_model
from src.models.explainability import get_feature_importance
from src.utils.logger import get_logger

logger = get_logger()


def main():
    # Load data
    X, y = load_training_data(
        feature_path="data/processed/features.csv",
        raw_data_path="data/raw/sample_data.csv",
    )

    # Load trained model
    model = joblib.load("models/baseline_model.joblib")

    # Predictions
    preds = model.predict(X)

    # Evaluation metrics
    metrics = evaluate_classification(y, preds)

    logger.info(f"Accuracy: {metrics['accuracy']}")
    logger.info("Confusion Matrix:")
    logger.info(f"\n{metrics['confusion_matrix']}")
    logger.info("Classification Report:")
    logger.info(f"\n{metrics['classification_report']}")

    # SAFE cross-validation (adaptive)
    cv_results = cross_validate_model(
        LogisticRegression(max_iter=1000),
        X,
        y,
    )

    if cv_results["cv_mean"] is None:
        logger.warning(cv_results["message"])
    else:
        logger.info(f"Cross-validation used cv={cv_results['cv_used']}")
        logger.info(f"Cross-validation mean accuracy: {cv_results['cv_mean']}")
        logger.info(f"Cross-validation std: {cv_results['cv_std']}")
        logger.info(f"All CV scores: {cv_results['all_scores']}")

    # Feature importance
    importance_df = get_feature_importance(model, X.columns)

    logger.info("Feature Importance:")
    logger.info(f"\n{importance_df}")


if __name__ == "__main__":
    main()

