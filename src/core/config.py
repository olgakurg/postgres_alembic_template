from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    some_setting: str


settings = Settings(_env_file=".env")


class LogSettings:
    dir: str = "logs"
    file: str = "app.txt"
    size: int = 1024 * 1024 * 20
    backup_num: int = 5


log_settings = LogSettings()
