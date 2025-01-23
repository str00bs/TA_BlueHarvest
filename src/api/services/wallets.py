"""File contains the WalletsService class."""

from logging import getLogger

from fastapi import status
from fastapi.exceptions import HTTPException
from masoniteorm.exceptions import QueryException

from api.schema import WalletsList, WalletsSchema
from databases.models import AccountsModel, WalletsModel

logger = getLogger(__name__)


class WalletsService:
    """Service class for the WalletsRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "DELETE"]

    def create(self, data: WalletsSchema):
        """Creates a `WalletsSchema` Entity from data"""
        # ? Check if account for wallet exists
        if not AccountsModel.find(data.account_id):
            account = AccountsModel.create(
                {"uuid": data.account_id, "is_anonymous": True}
            ).fresh()

        try:
            wallets = WalletsModel.create(data.model_dump()).fresh()
        except QueryException as e:
            logger.warning(e)
            raise HTTPException(
                status_code=409,
                detail="Wallets already exists",
            )
        return WalletsSchema(**wallets.serialize())

    def retrieve(self, uuid: str) -> WalletsSchema:
        """Retrieves a `WalletsSchema` Entity by uuid"""
        wallets = WalletsModel.find(uuid)

        if not wallets:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return WalletsSchema(**wallets.serialize())

    def listed(self, account_id: str, limit: int = 10, page_nr: int = 1) -> WalletsList:
        """Retrieves a `WalletsSchema` Entity by uuid"""
        if account_id:
            account = AccountsModel.find(account_id)
            if not account:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return WalletsList(data=account.wallets, meta=None)
        else:
            wallets = WalletsModel.simple_paginate(limit, page_nr)
            return WalletsList(**wallets.serialize())

    def delete(self, uuid: str) -> None:
        """Delete a `WalletsSchema` Entity by uuid"""
        wallets = WalletsModel.find(uuid)

        if not wallets:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            wallets.delete()
