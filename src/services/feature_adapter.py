import pandas as pd
from src.features.feature_builder import build_features


def build_features_from_request(payload: dict) -> pd.DataFrame:
    """
    Convert inference request into model-ready features.
    """
    df = pd.DataFrame([payload])
    features = build_features(df)
    return features
