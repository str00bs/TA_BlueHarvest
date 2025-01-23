"""
File contains response model/schema for the `Users` table
"""
from datetime import datetime
from random import choice
from secrets import token_urlsafe
from typing import List, Optional
from uuid import UUID, uuid4

from faker import Faker
from pydantic import BaseModel, EmailStr, Field, SecretStr, ConfigDict, field_serializer

from .generic import MetaSchema

fake = Faker()
fake_age = fake.random_int(min=25, max=55)
fake_name = fake.name()
fake_email = f"{fake_name.lower().replace(' ', '_')}{fake_age}@example.com"


class UsersSchema(BaseModel):
    """Model for a `Users` object"""

    uuid: UUID = Field(
        description="Unique IDentifier", default_factory=uuid4, alias="uuid"
    )

    name: str = Field(fake_name, description="Who to say users to")
    age: int = Field(fake_age, description="User age", gt=18, lt=110)
    email: EmailStr = Field(fake_email, description="User email")
    gender: Optional[str] = Field(
        choice(["Male", "Female", "Nonbinary"]),
        description="User gender identification",
    )

    # ? Private fields
    password: Optional[SecretStr] = Field(
        token_urlsafe(16), description="User password"
    )
    salt: Optional[SecretStr] = Field(
        token_urlsafe(128), description="Salt for password"
    )

    created_at: Optional[datetime] = Field(None, description="When the record was created")
    updated_at: Optional[datetime] = Field(
        None, description="When the record was last updated"
    )
    deleted_at: Optional[datetime] = Field(None, description="When the record was deleted")

    model_config = ConfigDict(from_attributes=True)

    def get_secrets(self):
        """Return a copy of the model with secrets"""
        return {
            "password": self.password.get_secret_value(),
            "salt": self.salt.get_secret_value(),
        }


class UsersList(BaseModel):
    """Model for a `Users` object"""

    data: List[UsersSchema]
    meta: MetaSchema
    model_config = ConfigDict(from_attributes=True)