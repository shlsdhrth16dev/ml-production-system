from src.pipelines.feature_pipeline import generate_features
from src.utils.logger import get_logger

logger = get_logger()


def main():
    features_df = generate_features("data/raw/sample_data.csv")

    output_path = "data/processed/features.csv"
    features_df.to_csv(output_path, index=False)

    logger.info(f"Feature generation complete. Saved to {output_path}")
    logger.info(f"Feature shape: {features_df.shape}")


if __name__ == "__main__":
    main()
