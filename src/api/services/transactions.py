"""File contains the TransactionsService class."""

from logging import getLogger
from uuid import UUID

from fastapi import status
from fastapi.exceptions import HTTPException

from api.schema import TransactionsList, TransactionsSchema
from databases.models import AccountsModel, TransactionsModel, WalletsModel

logger = getLogger(__name__)


class TransactionsService:
    """Service class for the TransactionsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST"]

    def create(self, data: TransactionsSchema):
        """Creates a `TransactionsSchema` Entity from data"""

        sender = WalletsModel.find(data.from_id)
        receiver = WalletsModel.find(data.to_id)
        if sender is None:
            raise HTTPException(
                status_code=404,
                detail="Sender (from) wallet not found",
            )
        if receiver is None:
            raise HTTPException(
                status_code=404,
                detail="Receiver (to) wallet not found",
            )
        if sender.balance < data.amount:
            raise HTTPException(
                status_code=409,
                detail="Insufficient funds",
            )

        sender.update({"balance": sender.balance - data.amount})
        receiver.update({"balance": receiver.balance + data.amount})
        transactions = TransactionsModel.create(data.model_dump()).fresh()

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

            return TransactionsList(data=account.get_transactions(), meta=None)
        elif wallet_id:
            wallet = WalletsModel.find(wallet_id)
            if not wallet:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return TransactionsList(data=wallet.transactions, meta=None)
        else:
            transactions = TransactionsModel.simple_paginate(limit, page_nr)
            return TransactionsList(**transactions.serialize())
