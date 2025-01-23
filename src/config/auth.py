"""File contains Auth Config Container"""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthConfig(BaseSettings):
    """Auth Config Container"""

    username: str = Field("admin", description="Basic Auth Username")
    password: str = Field("admin", description="Basic Auth Password")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="AUTH_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
