from src.pipelines.data_ingestion import load_and_validate_csv
from src.utils.logger import get_logger

logger = get_logger()


def main():
    df = load_and_validate_csv()
    logger.info(f"Validated dataset shape: {df.shape}")


if __name__ == "__main__":
    main()

