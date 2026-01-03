from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    app_name: str = Field(default="URL Shortner API")
    debug: bool = Field(default=False)
    api_v1_prefix: str = Field(default="/api/v1")

    # Database
    database_url: str = Field(...)

    # Redis
    redis_url: str = Field(...)

    # Security
    secret_key: str = Field(...)
    algorithm: str = Field(default="H256")
    access_token_expire_minutes: int = Field(default=30)

    class Config:
        env_file = ".env"
        case_sensitive = False

# Create global settings instance
settings = Settings()