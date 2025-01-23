"""File contains the PreferencesService class."""
from typing import List
from logging import getLogger

from masoniteorm.exceptions import QueryException
from fastapi import status
from fastapi.exceptions import HTTPException

from api.schema import PreferencesSchema, PreferencesList
from databases.models import PreferencesModel

logger = getLogger(__name__)


class PreferencesService:
    """Service class for the PreferencesRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: PreferencesSchema):
        """Creates a `PreferencesSchema` Entity from data"""
        try:
            preferences = PreferencesModel.create(data.model_dump()).fresh()
        except QueryException as e:
            logger.warning(e)
            raise HTTPException(
                status_code=409,
                detail="Preferences already exists",
            )
        return PreferencesSchema(**preferences.serialize())

    def retrieve(self, uuid: str) -> PreferencesSchema:
        """Retrieves a `PreferencesSchema` Entity by uuid"""
        preferences = PreferencesModel.find(uuid)

        if not preferences:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return PreferencesSchema(**preferences.serialize())

    def listed(
        self, limit: int = 10, page_nr: int = 1
    ) -> PreferencesList:
        """Retrieves a `PreferencesSchema` Entity by uuid"""
        preferences = PreferencesModel.simple_paginate(
            limit, page_nr
        )
        return PreferencesList(**preferences.serialize())

    def update(self, uuid: str, data: PreferencesSchema) -> PreferencesSchema:
        """Updates a `PreferencesSchema` Entity by uuid with data"""
        preferences = PreferencesModel.find(uuid)

        if not preferences:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            preferences.update(data.model_dump())

        return PreferencesSchema(**preferences.serialize())

    def delete(self, uuid: str) -> None:
        """Delete a `PreferencesSchema` Entity by uuid"""
        preferences = PreferencesModel.find(uuid)

        if not preferences:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            preferences.delete()

    def replace(self, uuid: str, data: PreferencesSchema) -> PreferencesSchema:
        """Replaces a `PreferencesSchema` Entity by uuid with data"""
        preferences = PreferencesModel.find(uuid)

        if not preferences:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        preferences = preferences.serialize()
        preferences.update(data)
        self.delete(uuid)
        return self.create(data)
