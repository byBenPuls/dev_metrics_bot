from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


class TelegramSettings(BaseSettings):
    BOT_TOKEN: str
    BOT_WEBHOOK_HOST: str
    BOT_WEBHOOK_URL: str


class GitHubSettings(BaseSettings):
    GITHUB_TOKEN: str


class Settings(
    RedisSettings,
    TelegramSettings,
    GitHubSettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
