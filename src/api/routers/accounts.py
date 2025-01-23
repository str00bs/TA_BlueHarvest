"""File contains endpoint router for '/accounts'"""

from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Security

from api.auth import Auth
from api.responses import AccountsResponses
from api.services import AccountsService

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/accounts",
    tags=["Accounts"],
    dependencies=[Security(Auth.basic)],
)


@router.get(
    path="/overview/{uuid}",
    operation_id="api.accounts.overview",
    responses=AccountsResponses.overview,
)
async def account_overview(
    uuid: UUID = Path(
        description="Unique Identifier for the Accounts Entity to retrieve"
    ),
    service=Depends(AccountsService),
):
    """Endpoint is used to retrieve a `Accounts` entity"""
    result = service.overview(uuid)
    return result
