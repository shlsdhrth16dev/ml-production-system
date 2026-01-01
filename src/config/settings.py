from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    project_name: str
    env: str
    log_level: str
    data_dir: str

    class Config:
        env_file = BASE_DIR / ".env"

settings = Settings()

