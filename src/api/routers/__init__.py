from .accounts import router as accounts_router
from .crud import crud_routers
from .system import router as system_router

routers = [
    system_router,
    accounts_router,
    *crud_routers,
]
