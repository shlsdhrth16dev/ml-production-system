from loguru import logger
import sys
from src.config.settings import settings

LOG_LEVEL = settings.log_level.upper()

logger.remove()
logger.add(
    sys.stdout,
    level=LOG_LEVEL,
    format="<green>{time}</green> | <level>{level}</level> | <level>{message}</level>",
)

def get_logger():
    return logger


