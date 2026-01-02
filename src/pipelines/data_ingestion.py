import pandas as pd
from typing import List

from src.config.schema import LoanRecord
from src.utils.logger import get_logger

logger = get_logger()

RAW_DATA_PATH = "data/raw/loan_data/load_data.csv"


def load_and_validate_csv(path: str = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load raw loan data and validate each row against the LoanRecord schema.
    """

    logger.info(f"Loading raw data from {path}")
    df = pd.read_csv(path)

    logger.info(f"Validating {len(df)} records against schema")

    validated_records: List[LoanRecord] = []

    for idx, row in df.iterrows():
        try:
            record = LoanRecord(**row.to_dict())
            validated_records.append(record)
        except Exception as e:
            logger.error(f"Schema validation failed at row {idx}: {e}")
            raise

    logger.info("All records successfully validated")

    # Convert back to DataFrame (validated, typed)
    validated_df = pd.DataFrame([r.model_dump() for r in validated_records])

    return validated_df

