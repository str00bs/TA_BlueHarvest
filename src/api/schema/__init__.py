"""Module loads and contains API Schema"""
from .generic import MetaSchema, MessageSchema
from .preferences import PreferencesSchema, PreferencesList
from .users import UsersSchema, UsersList

__all__ = [
    "MetaSchema",
    "MessageSchema",
    "PreferencesSchema",
    "PreferencesList",
    "UsersSchema",
    "UsersList"
]
