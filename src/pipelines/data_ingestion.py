import pandas as pd
from typing import List
from src.data_schema import RawRecord


def load_and_validate_csv(path: str) -> List[RawRecord]:
    df = pd.read_csv(path)

    records: List[RawRecord] = []
    for _, row in df.iterrows():
        record = RawRecord(**row.to_dict())
        records.append(record)

    return records
