"""File contains generic models"""
from typing import List, Optional

from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    """Generic message model"""

    msg: str


class MetaSchema(BaseModel):
    """Generic meta model"""

    count: int = Field(..., description="Total number of items in the list")
    current_page: int = Field(..., description="Current page of the list")
    next_page: Optional[int] = Field(..., description="Next page of the list")
    previous_page: Optional[int] = Field(..., description="Previous page of the list")
