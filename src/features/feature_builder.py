import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform validated raw data into model-ready features.
    This function must be deterministic and leakage-free.
    """

    features = pd.DataFrame()

    # Basic numeric features
    features["age"] = df["age"]
    features["income"] = df["income"]
    features["loan_amount"] = df["loan_amount"]

    # Derived features
    features["income_to_loan_ratio"] = df["income"] / (df["loan_amount"] + 1)

    return features
