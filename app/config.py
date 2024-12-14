from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "mobile.sqlite3"

class Settings(BaseSettings):
    
    #url: str = "postgresql+asyncpg://efUser:efPassword@db:5432/efDB"
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()