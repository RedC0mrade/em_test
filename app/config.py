from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# BASE_DIR = Path(__file__).parent.parent
# DB_PATH = BASE_DIR / "mobile.sqlite3"

class Settings(BaseSettings):
    
    url: str = "postgresql+asyncpg://emUser:emPassword@db:5432/emDB"
    url_test: str = f"sqlite+aiosqlite:///:memory:"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()