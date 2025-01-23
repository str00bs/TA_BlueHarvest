"""File contains endpoint router for '/wallets'"""

from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query, Security, status
from fastapi.responses import Response

from api.auth import Auth
from api.responses.wallets import WalletsResponses
from api.schema.wallets import WalletsList, WalletsSchema
from api.services.wallets import WalletsService

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/wallets",
    tags=["Wallets CRUD"],
    dependencies=[Security(Auth.basic)],
)


# ? Router CRUD Endpoints
@router.options(
    path="/wallets",
    operation_id="api.wallets.options",
    responses=WalletsResponses.options,
)
async def wallets_options(service=Depends(WalletsService)):
    """Endpoint is used to find options for the `Wallets` router"""
    result = service.options()

    return Response(headers={"allow": str(result)})


@router.post(
    path="/wallets",
    operation_id="api.wallets.create",
    responses=WalletsResponses.create,
    status_code=201,
)
async def create_wallet(
    wallets: WalletsSchema,
    service=Depends(WalletsService),
):
    """Endpoint is used to create a `Wallets` entity"""
    result = service.create(data=wallets)

    return result


@router.get(
    path="/wallets",
    operation_id="api.wallets.listed",
    responses=WalletsResponses.listed,
)
async def retrieve_wallets_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    account_id: UUID = Query(None, description="Account ID to filter wallets by"),
    service=Depends(WalletsService),
) -> WalletsList:
    """Endpoint is used to retrieve a list of `Wallets` entities"""
    result = service.listed(account_id=account_id, limit=limit, page_nr=page_nr)

    return result


@router.get(
    path="/wallets/{uuid}",
    operation_id="api.wallets.retrieve",
    responses=WalletsResponses.retrieve,
)
async def retrieve_wallet(
    uuid: UUID = Path(
        description="Unique Identifier for the Wallets Entity to retrieve",
    ),
    service=Depends(WalletsService),
):
    """Endpoint is used to retrieve a `Wallets` entity"""

    result = service.retrieve(uuid)

    return result


@router.delete(
    path="/wallets/{uuid}",
    operation_id="api.wallets.delete",
    responses=WalletsResponses.delete,
    status_code=204,
)
async def delete_wallet(
    uuid: str = Path(
        ...,
        description="Unique Identifier for the Wallets Entity to delete",
    ),
    service=Depends(WalletsService),
):
    """Endpoint is used to delete a `Wallets` entity"""
    service.delete(uuid)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
