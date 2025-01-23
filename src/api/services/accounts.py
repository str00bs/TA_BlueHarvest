"""File contains the AccountsService class."""

from logging import getLogger
from typing import List

from fastapi import status
from fastapi.exceptions import HTTPException
from masoniteorm.exceptions import QueryException

from api.schema import (AccountsList, AccountsSchema, OverviewSchema,
                        TransactionsSchema, WalletsSchema)
from databases.models import AccountsModel, TransactionsModel

logger = getLogger(__name__)


class AccountsService:
    """Service class for the AccountsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def overview(self, uuid: str) -> OverviewSchema:
        """Registers a new `Account` Entity from data"""
        account = AccountsModel.find(uuid)
        if not account:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        try:
            transactions = [
                TransactionsSchema(**transaction)
                for transaction in TransactionsModel.where_in("from_id", account.wallets.pluck("uuid")).get().serialize()
            ]
            wallets = [
                WalletsSchema(**wallet) for wallet in account.wallets.serialize()
            ]

        except AttributeError as ex:
            logger.warning(ex)
            raise HTTPException(404, detail="Wallets not found")

        overview = OverviewSchema(
            account=AccountsSchema(**account.serialize()),
            wallets=wallets,
            transactions=transactions,
        )
        return overview

    # ? CRUD Operations
    def create(self, data: AccountsSchema):
        """Creates a `AccountsSchema` Entity from data"""
        try:
            secrets = data.get_secrets()
            data = data.model_dump()
            data.update(secrets)
            account = AccountsModel.create(data).fresh()
        except QueryException as e:
            logger.warning(e)
            raise HTTPException(
                status_code=409,
                detail="Account already exists",
            )

        return AccountsSchema(**account.serialize())

    def retrieve(self, uuid: str) -> AccountsSchema:
        """Retrieves a `AccountsSchema` Entity by uuid"""
        account = AccountsModel.find(uuid)

        if not account:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return AccountsSchema(**account.serialize())

    def listed(
        self, limit: int = 10, page_nr: int = 1, **kwargs
    ) -> List[AccountsSchema]:
        """Retrieves a `AccountsSchema` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        account = AccountsModel.simple_paginate(limit, page_nr)
        return AccountsList(**account.serialize())

    def update(self, uuid: str, data: AccountsSchema) -> AccountsSchema:
        """Updates a `AccountsSchema` Entity by uuid with data"""
        account = AccountsModel.find(uuid)

        if not account:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            account.update(data.model_dump(exclude_defaults=True, exclude=["uuid"]))

        return AccountsSchema(**account.serialize())

    def replace(self, uuid: str, data: AccountsSchema) -> AccountsSchema:
        """Replaces a `AccountsSchema` Entity by uuid with data"""
        account = AccountsModel.find(uuid)

        if not account:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> None:
        """Delete a `AccountsSchema` Entity by uuid"""
        account = AccountsModel.find(uuid)
        if not account:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            account.delete()

    def deleted(self, limit: int = 10, page_nr: int = 1) -> List[AccountsSchema]:
        account = AccountsModel.only_trashed().simple_paginate(limit, page_nr)
        return AccountsList(**account.serialize())
