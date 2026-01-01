from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger()

def main():
    logger.info("Project bootstrapped successfully")
    logger.info(f"Environment: {settings.env}")
    logger.info(f"Data directory: {settings.data_dir}")

if __name__ == "__main__":
    main()



