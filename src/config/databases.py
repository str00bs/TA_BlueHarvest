"""
File contains DATABASE configurations
"""
from pathlib import Path
from typing import Union, Optional

from masoniteorm.connections import ConnectionResolver
from pydantic import Field, root_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseSettings):
    """
    Partial used by the DatabaseConfig container providing
    the main configuration used to initilize the DB.
    """

    host: str = Field(None)
    port: int = Field(None)
    database: Union[str, Path] = Field(...)

    driver: str = Field(...)
    driver_default: str = Field(...)
    log_queries: bool = Field(None)

    user: str = Field(...)
    password: str = Field(...)
    root_user: Optional[str] = Field(None)
    root_password: Optional[str] = Field(None)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


class DatabaseConfig(BaseSettings):
    """
    Container for all Database configs
    """

    databases: dict = Database().model_dump()

    @root_validator(skip_on_failure=True)
    def parse_to_orm_format(cls, values):
        """
        Organizing the settings in the way expected by the ORM.

        This is is a non-breaking constraint of the current version
        and will be addressed in a future release.
        """
        _copy: dict = values.copy()
        _default = _copy["databases"].pop("driver_default")
        values["databases"] = {
            "default": _default,
            _default: _copy["databases"],
        }
        return values


DB = ConnectionResolver().set_connection_details(DatabaseConfig().databases)
