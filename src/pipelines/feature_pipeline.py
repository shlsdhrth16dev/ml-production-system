import pandas as pd
from src.pipelines.data_ingestion import load_and_validate_csv
from src.features.feature_builder import build_features


def generate_features(raw_data_path: str) -> pd.DataFrame:
    # Load and validate raw records
    records = load_and_validate_csv(raw_data_path)

    # Convert validated records to DataFrame
    df = pd.DataFrame([r.model_dump() for r in records])

    # Build features
    features_df = build_features(df)

    return features_df
