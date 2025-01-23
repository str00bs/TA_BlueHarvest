"""File contains endpoint router for '/accounts'"""

from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, Path, Query, Security, status
from fastapi.responses import Response

from api.auth import Auth
from api.responses import AccountsResponses
from api.schema import AccountsList, AccountsSchema
from api.services import AccountsService
from api.tasks import AccountsTasks

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/accounts",
    tags=["Accounts CRUD"],
    dependencies=[Security(Auth.basic)],
)


@router.options(
    path="/", operation_id="api.accounts.options", responses=AccountsResponses.options
)
async def accounts_options(service=Depends(AccountsService)) -> AccountsSchema:
    """Endpoint is used to find options for the `Accounts` router"""
    result = service.options()
    return Response(headers={"allow": str(result)})


# ? CRUD Endpoints
@router.post(
    path="/",
    operation_id="api.accounts.create",
    responses=AccountsResponses.create,
    status_code=201,
)
async def create_account(
    accounts: AccountsSchema,
    background: BackgroundTasks,
    service=Depends(AccountsService),
) -> AccountsSchema:
    """Endpoint is used to create a `Accounts` entity"""
    result = service.create(accounts)

    # ? Is executed after the router has returned a response
    background.add_task(AccountsTasks.do_after, entity=result)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.accounts.retrieve",
    responses=AccountsResponses.retrieve,
)
async def retrieve_account(
    uuid: UUID = Path(
        description="Unique Identifier for the Accounts Entity to retrieve"
    ),
    service=Depends(AccountsService),
) -> AccountsSchema:
    """Endpoint is used to retrieve a `Accounts` entity"""
    result = service.retrieve(uuid)

    return result


@router.get(
    path="/", operation_id="api.accounts.listed", responses=AccountsResponses.listed
)
async def retrieve_accounts_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(AccountsService),
) -> AccountsList:
    """Endpoint is used to retrieve a list of `Accounts` entities"""
    result = service.listed(limit=limit, page_nr=page_nr)

    return result


@router.get(
    path="/deleted",
    operation_id="api.accounts.deleted",
    responses=AccountsResponses.listed,
)
async def retrieve_deleted_accounts(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(AccountsService),
) -> AccountsList:
    """Endpoint is used to retrieve a list of `Accounts` entities"""
    result = service.deleted(limit=limit, page_nr=page_nr)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.accounts.replace",
    responses=AccountsResponses.replace,
)
async def replace_account(
    accounts: AccountsSchema,
    uuid: str = Path(
        ..., description="Unique Identifier for the Accounts Entity to update"
    ),
    service=Depends(AccountsService),
) -> AccountsSchema:
    """Endpoint is used to replace a `Accounts` entity"""
    result = service.replace(uuid, accounts)

    return result


@router.patch(
    path="/{uuid}",
    operation_id="api.accounts.update",
    responses=AccountsResponses.update,
)
async def update_account(
    accounts: AccountsSchema,
    uuid: str = Path(
        ..., description="Unique Identifier for the Accounts Entity to update"
    ),
    service=Depends(AccountsService),
) -> AccountsSchema:
    """Endpoint is used to update a `Accounts` entity"""
    result = service.update(uuid, accounts)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.accounts.delete",
    responses=AccountsResponses.delete,
    status_code=204,
)
async def delete_account(
    uuid: str = Path(
        ..., description="Unique Identifier for the Accounts Entity to delete"
    ),
    service=Depends(AccountsService),
) -> None:
    """Endpoint is used to delete a `Accounts` entity"""
    service.delete(uuid)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
