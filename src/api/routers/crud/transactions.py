"""File contains endpoint router for '/transactions'"""

from logging import getLogger
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query, Security
from fastapi.responses import Response

from api.auth import Auth
from api.responses.transactions import TransactionsResponses
from api.schema.transactions import TransactionsList, TransactionsSchema
from api.services.transactions import TransactionsService

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/transactions",
    tags=["Transactions CRUD"],
    dependencies=[Security(Auth.basic)],
)


@router.options(
    path="/",
    operation_id="api.transactions.options",
    responses=TransactionsResponses.options,
)
async def transactions_options(service=Depends(TransactionsService)):
    """Endpoint is used to find options for the `Transactions` router"""
    result = service.options()

    return Response(headers={"allow": str(result)})


# ? Router CRUD Endpoints
@router.post(
    path="/",
    operation_id="api.transactions.create",
    responses=TransactionsResponses.create,
    status_code=201,
)
async def create_transaction(
    transactions: TransactionsSchema,
    service=Depends(TransactionsService),
):
    """Endpoint is used to create a `Transactions` entity"""
    result = service.create(transactions)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.transactions.retrieve",
    responses=TransactionsResponses.retrieve,
)
async def retrieve_transaction(
    uuid: UUID = Path(
        description="Unique Identifier for the Transactions Entity to retrieve",
    ),
    service=Depends(TransactionsService),
):
    """Endpoint is used to retrieve a `Transactions` entity"""

    result = service.retrieve(uuid)

    return result


@router.get(
    path="/",
    operation_id="api.transactions.listed",
    responses=TransactionsResponses.listed,
)
async def retrieve_transactions_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    account_id: Optional[UUID] = Query(
        None, descritpion="Account ID to filter transactions by"
    ),
    wallet_id: Optional[UUID] = Query(
        None, descritpion="Wallet ID to filter transactions by"
    ),
    service=Depends(TransactionsService),
) -> TransactionsList:
    """Endpoint is used to retrieve a list of `Transactions` entities"""
    result = service.listed(
        limit=limit, page_nr=page_nr, account_id=account_id, wallet_id=wallet_id
    )

    return result
