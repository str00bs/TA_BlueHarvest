"""Module loads and contains API Routers"""

from .accounts import router as accounts_router
from .transactions import router as transactions_router
from .wallets import router as wallets_router

crud_routers = [accounts_router, wallets_router, transactions_router]
