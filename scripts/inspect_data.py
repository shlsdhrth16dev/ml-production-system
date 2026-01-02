import pandas as pd
from pathlib import Path


DATA_PATH = Path("data/raw/loan_data/load_data.csv")


def inspect_dataset(path: Path):
    print("=" * 80)
    print(f"Inspecting dataset: {path}")
    print("=" * 80)

    df = pd.read_csv(path)

    # Basic shape
    print("\n📐 Shape:")
    print(df.shape)

    # Columns
    print("\n📊 Columns:")
    for col in df.columns:
        print(f"- {col}")

    # Data types
    print("\n🧬 Data types:")
    print(df.dtypes)

    # Missing values
    print("\n🚨 Missing values (count):")
    print(df.isnull().sum())

    # Sample rows
    print("\n🔍 Sample rows:")
    print(df.head())

    # Target distribution (if target exists)
    possible_targets = ["target", "loan_status", "default", "label"]

    for col in possible_targets:
        if col in df.columns:
            print("\n🎯 Target distribution:")
            print(df[col].value_counts())
            break
    else:
        print("\n⚠️ No obvious target column found.")


if __name__ == "__main__":
    inspect_dataset(DATA_PATH)

