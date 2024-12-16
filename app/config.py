from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    url: str = "postgresql+asyncpg://emUser:emPassword@db:5432/emDB"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()