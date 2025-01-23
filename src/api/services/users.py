"""File contains the UsersService class."""
from typing import List
from logging import getLogger
from masoniteorm.exceptions import QueryException
from fastapi import status
from fastapi.exceptions import HTTPException
from api.schema import UsersSchema, UsersList
from databases.models import UsersModel

logger = getLogger(__name__)


class UsersService:
    """Service class for the UsersRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: UsersSchema):
        """Creates a `UsersSchema` Entity from data"""
        try:
            secrets = data.get_secrets()
            data = data.model_dump()
            data.update(secrets)
            user = UsersModel.create(data).fresh()
        except QueryException as e:
            logger.warning(e)
            raise HTTPException(
                status_code=409,
                detail="User already exists",
            )

        return UsersSchema(**user.serialize())

    def retrieve(self, uuid: str) -> UsersSchema:
        """Retrieves a `UsersSchema` Entity by uuid"""
        user = UsersModel.find(uuid)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return UsersSchema(**user.serialize())

    def listed(
        self, limit: int = 10, page_nr: int = 1, **kwargs
    ) -> List[UsersSchema]:
        """Retrieves a `UsersSchema` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        user = UsersModel.simple_paginate(limit, page_nr)
        return UsersList(**user.serialize())

    def update(self, uuid: str, data: UsersSchema) -> UsersSchema:
        """Updates a `UsersSchema` Entity by uuid with data"""
        user = UsersModel.find(uuid)
    
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            user.update(data.model_dump(exclude_defaults=True, exclude=["uuid"]))

        return UsersSchema(**user.serialize())

    def replace(self, uuid: str, data: UsersSchema) -> UsersSchema:
        """Replaces a `UsersSchema` Entity by uuid with data"""
        user = UsersModel.find(uuid)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> None:
        """Delete a `UsersSchema` Entity by uuid"""
        user = UsersModel.find(uuid)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            user.delete()

    def deleted(
        self, limit: int = 10, page_nr: int = 1
    ) -> List[UsersSchema]:
        user = UsersModel.only_trashed().simple_paginate(limit, page_nr)
        return UsersList(**user.serialize())
