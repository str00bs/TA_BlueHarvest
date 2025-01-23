"""File contains endpoint router for '/preferences'"""
from logging import getLogger
from uuid import UUID

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    Path,
    Query,
    Security,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from api.auth import Auth
from api.responses.preferences import PreferencesResponses
from api.schema.preferences import PreferencesSchema, PreferencesList
from api.services.preferences import PreferencesService

# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/preferences",
    tags=["Preferences CRUD"],
    dependencies=[Security(Auth.basic)],
)

# ? Router CRUD Endpoints
@router.options(
    path="/",
    operation_id="api.preferences.options",
    responses=PreferencesResponses.options,
)
async def preferences_options(service=Depends(PreferencesService)):
    """Endpoint is used to find options for the `Preferences` router"""
    result = service.options()

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.preferences.create",
    responses=PreferencesResponses.create,
    status_code=201,
)
async def create_preferences(
    preferences: PreferencesSchema,
    service=Depends(PreferencesService),
):
    """Endpoint is used to create a `Preferences` entity"""
    result = service.create(preferences)

    return result


@router.get(
    path="/", operation_id="api.preferences.listed", responses=PreferencesResponses.listed
)
async def retrieve_preferences_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(PreferencesService),
) -> PreferencesList:
    """Endpoint is used to retrieve a list of `Preferences` entities"""
    result = service.listed(limit=limit, page_nr=page_nr)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.preferences.retrieve",
    responses=PreferencesResponses.retrieve,
)
async def retrieve_preferences(
    uuid: UUID = Path(
        description="Unique Identifier for the Preferences Entity to retrieve",
    ),
    service=Depends(PreferencesService),
):
    """Endpoint is used to retrieve a `Preferences` entity"""

    result = service.retrieve(uuid)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.preferences.replace",
    responses=PreferencesResponses.replace,
)
async def replace_preferences(
    preferences: PreferencesSchema,
    uuid: str = Path(
        ...,
        description="Unique Identifier for the Preferences Entity to update",
    ),
    service=Depends(PreferencesService),
):
    """Endpoint is used to replace a `Preferences` entity"""
    result = service.replace(uuid, preferences)

    return result


@router.patch(
    path="/{uuid}",
    operation_id="api.preferences.update",
    responses=PreferencesResponses.update,
)
async def update_preferences(
    preferences: PreferencesSchema,
    uuid: str = Path(
        ...,
        description="Unique Identifier for the Preferences Entity to update",
    ),
    service=Depends(PreferencesService),
):
    """Endpoint is used to update a `Preferences` entity"""
    result = service.update(uuid, preferences)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.preferences.delete",
    responses=PreferencesResponses.delete,
    status_code=204,
)
async def delete_preferences(
    uuid: str = Path(
        ...,
        description="Unique Identifier for the Preferences Entity to delete",
    ),
    service=Depends(PreferencesService),
):
    """Endpoint is used to delete a `Preferences` entity"""
    service.delete(uuid)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
