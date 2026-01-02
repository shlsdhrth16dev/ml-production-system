from src.pipelines.data_ingestion import load_and_validate_csv
from src.utils.logger import get_logger

logger = get_logger()


def main():
    records = load_and_validate_csv("data/raw/sample_data.csv")
    logger.info(f"Successfully validated {len(records)} records")


if __name__ == "__main__":
    main()

