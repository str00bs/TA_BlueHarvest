"""Module loads and contains API Responses"""
from .generic import GenericResponses
from .preferences import PreferencesResponses
from .system import SystemResponses
from .users import UsersResponses


__all__ = [
    "GenericResponses",
    "PreferencesResponses",
    "SystemResponses",
    "UsersResponses"
]
