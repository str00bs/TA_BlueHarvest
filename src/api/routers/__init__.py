"""Module loads and contains API Routers"""
from .preferences import router as preferences_router
from .system import router as system_router
from .users import router as users_router

routers = [
    preferences_router,
    system_router,
    users_router
]
