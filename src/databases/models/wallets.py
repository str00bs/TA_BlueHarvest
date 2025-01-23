"""
File contains wallets model
"""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import UUIDPrimaryKeyMixin

from databases.observers.wallets import WalletsObserver


class WalletsModel(Model, UUIDPrimaryKeyMixin):
    """
    Database ORM Model for 'wallets'
    """

    # __connection__ = 'NAME'
    __table__ = "wallets"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []

    @has_many("uuid", "from_id")
    def transactions(self):
        from databases.models.transactions import TransactionsModel

        return TransactionsModel


WalletsModel.observe(WalletsObserver())
