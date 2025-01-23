"""
File contains transactions model
"""

from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin


class TransactionsModel(Model, UUIDPrimaryKeyMixin):
    """
    Database ORM Model for 'transactions'
    """

    # __connection__ = 'NAME'
    __table__ = "transactions"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []
