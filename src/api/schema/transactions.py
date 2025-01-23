"""
File contains response model/schema for the `Transactions` table
"""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field

from api.schema.generic import MetaSchema


class TransactionsSchema(BaseModel):
    """Model for a `Transactions` object"""

    uuid: UUID = Field(description="Unique IDentifier", default_factory=uuid4)

    amount: Decimal = Field(0.0, description="Amount in the transaction")
    description: Optional[str] = Field(
        None, description="Description of the transaction"
    )
    from_id: UUID = Field(
        description="Which wallet sends the transaction", default_factory=uuid4
    )
    to_id: UUID = Field(
        description="Which wallet receives the transaction", default_factory=uuid4
    )

    created_at: Optional[datetime] = Field(
        None, description="When the record was created"
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="When the record was last updated",
    )

    model_config = ConfigDict(from_attributes=True)


class TransactionsList(BaseModel):
    """Model for a `Transactions` object"""

    data: List[TransactionsSchema]
    meta: Optional[MetaSchema]
    model_config = ConfigDict(from_attributes=True)
