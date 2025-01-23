"""
Module contains standardized config loader and management.
This is implemented using Pydantic for type safety and docker secerts support.
"""
from .api import APIConfig
from .auth import AuthConfig
from .databases import DatabaseConfig


class ConfigContainer:
    Api: APIConfig = APIConfig()
    Auth: AuthConfig = AuthConfig()
    Database: DatabaseConfig = DatabaseConfig()


Config = ConfigContainer()
