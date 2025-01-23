"""File contains the TransactionsService class."""

from logging import getLogger
from uuid import UUID

from fastapi import status
from fastapi.exceptions import HTTPException
from masoniteorm.exceptions import QueryException

from api.schema import TransactionsList, TransactionsSchema
from databases.models import AccountsModel, TransactionsModel, WalletsModel

logger = getLogger(__name__)


class TransactionsService:
    """Service class for the TransactionsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST"]

    def create(self, data: TransactionsSchema):
        """Creates a `TransactionsSchema` Entity from data"""
        try:
            transactions = TransactionsModel.create(data.model_dump()).fresh()
            WalletsModel.find(data.wallet_id).update({"balance": data.amount})

        except QueryException as e:
            logger.warning(e)
            raise HTTPException(
                status_code=409,
                detail="Transactions already exists",
            )
        return TransactionsSchema(**transactions.serialize())

    def retrieve(self, uuid: str) -> TransactionsSchema:
        """Retrieves a `TransactionsSchema` Entity by uuid"""
        transactions = TransactionsModel.find(uuid)

        if not transactions:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return TransactionsSchema(**transactions.serialize())

    def listed(
        self,
        limit: int = 10,
        page_nr: int = 1,
        account_id: UUID = None,
        wallet_id: UUID = None,
    ) -> TransactionsList:
        """Retrieves a `TransactionsSchema` Entity by uuid"""

        if account_id:
            account = AccountsModel.find(account_id)
            if not account:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return TransactionsList(data=account.transactions, meta=None)
        elif wallet_id:
            wallet = WalletsModel.find(wallet_id)
            if not wallet:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return TransactionsList(data=wallet.transactions, meta=None)
        else:
            transactions = TransactionsModel.simple_paginate(limit, page_nr)
            return TransactionsList(**transactions.serialize())
