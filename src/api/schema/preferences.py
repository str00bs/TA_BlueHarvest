"""
File contains response model/schema for the `Preferences` table
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict

from api.schema import MetaSchema


class PreferencesSchema(BaseModel):
    """Model for a `Preferences` object"""

    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    user_id: UUID = Field(
        description="User the preferences belongs to", default_factory=uuid4
    )

    toggle_dark_mode: bool = Field(True, description="Toggle dark mode")
    toggle_email: bool = Field(True, description="Toggle email")
    toggle_notifications: bool = Field(
        True, description="Toggle notifications"
    )

    created_at: Optional[datetime] = Field(None, description="When the record was created")
    updated_at: Optional[datetime] = Field(
        None, description="When the record was last updated",
    )

    model_config = ConfigDict(from_attributes=True)


class PreferencesList(BaseModel):
    """Model for a `Preferences` object"""

    data: List[PreferencesSchema]
    meta: MetaSchema
    model_config = ConfigDict(from_attributes=True)