"""Module loads and contains API Responses"""

from .accounts import AccountsResponses
from .generic import GenericResponses
from .system import SystemResponses
from .transactions import TransactionsResponses
from .wallets import WalletsResponses

__all__ = [
    "GenericResponses",
    "WalletsResponses",
    "SystemResponses",
    "AccountsResponses",
    "TransactionsResponses",
]
