"""
File contains response model/schema for the `Wallets` table
"""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field

from api.schema.generic import MetaSchema


class WalletsSchema(BaseModel):
    """Model for a `Wallets` object"""

    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)
    account_id: UUID = Field(
        description="Account the wallet belongs to", default_factory=uuid4
    )

    balance: Decimal = Field(0.0, description="Wallet balance")

    created_at: Optional[datetime] = Field(
        None, description="When the record was created"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="When the record was last updated",
    )

    model_config = ConfigDict(from_attributes=True)


class WalletsList(BaseModel):
    """Model for a `Wallets` object"""

    data: List[WalletsSchema]
    meta: Optional[MetaSchema]
    model_config = ConfigDict(from_attributes=True)
