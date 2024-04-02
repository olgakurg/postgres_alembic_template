from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_echo: bool = False


settings = Settings(_env_file=".env")


class LogSettings:
    dir: str = "logs"
    file: str = "app.txt"
    size: int = 1024 * 1024 * 20
    backup_num: int = 5


log_settings = LogSettings()
