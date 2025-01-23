"""Module contains and loads Database Models"""
from .users import UsersModel
from .preferences import PreferencesModel

__all__ = [
    "UsersModel",
    "PreferencesModel",
]
