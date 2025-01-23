"""
File contains response model/schema for the `Accounts` table
"""

from datetime import datetime
from decimal import Decimal
from random import choice
from secrets import token_urlsafe
from typing import List, Optional
from uuid import UUID, uuid4

from faker import Faker
from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr

from api.schema.generic import MetaSchema
from api.schema.transactions import TransactionsSchema
from api.schema.wallets import WalletsSchema

fake = Faker()
fake_first_name = fake.first_name()
fake_last_name = fake.last_name()
fake_age = fake.random_int(min=25, max=55)
fake_email = (
    f"{fake_first_name.lower()}_{fake_last_name.lower()}" f"{fake_age}@example.com"
)


class AccountsSchema(BaseModel):
    """Model for a `Accounts` object"""

    uuid: UUID = Field(
        description="Unique IDentifier", default_factory=uuid4, alias="uuid"
    )

    # ? Private fields
    type_: str = Field(
        choice(["customer", "admin"]),
        description="Account type",
        alias="type",
        exclude=True,
    )
    is_anonymous: bool = Field(
        False, description="Is the account registered", exclude=True
    )

    # ? Public fields
    first_name: str = Field(fake_first_name, description="Account first name")
    last_name: str = Field(fake_last_name, description="Account last name")
    age: int = Field(fake_age, description="Account age", gt=18, lt=110)
    email: EmailStr = Field(fake_email, description="Account email")
    initial_balance: Decimal = Field(0, description="Initial credit for account", ge=0)

    # ? Secret fields
    password: Optional[SecretStr] = Field(
        token_urlsafe(16), description="Account password", exclude=True
    )
    salt: Optional[SecretStr] = Field(
        token_urlsafe(128), description="Salt for password", exclude=True
    )

    created_at: Optional[datetime] = Field(
        None, description="When the record was created"
    )
    updated_at: Optional[datetime] = Field(
        None, description="When the record was last updated"
    )
    deleted_at: Optional[datetime] = Field(
        None, description="When the record was deleted", exclude=True
    )

    model_config = ConfigDict(from_attributes=True)

    def get_secrets(self):
        """Return a copy of the model with secrets"""
        return {
            "password": self.password.get_secret_value(),
            "salt": self.salt.get_secret_value(),
        }


class AccountsList(BaseModel):
    """Model for a `Accounts` object"""

    data: List[AccountsSchema]
    meta: MetaSchema
    model_config = ConfigDict(from_attributes=True)


class OverviewSchema(BaseModel):
    """Schema for overview of `Account` and child objects"""

    account: AccountsSchema = Field(..., description="Account to register")
    wallets: List[WalletsSchema] = Field(..., description="Wallet to register")
    transactions: List[TransactionsSchema] = Field(
        ..., description="Transactions for account"
    )
