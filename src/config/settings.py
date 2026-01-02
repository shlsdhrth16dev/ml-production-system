from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    project_name: str
    env: str
    log_level: str
    data_dir: str

    model_config = ConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",   # 👈 THIS IS THE FIX
    )


settings = Settings()

