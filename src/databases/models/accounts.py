"""
File contains accounts model
"""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin

from databases.observers.accounts import AccountsObserver


class AccountsModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """
    Database ORM Model for 'accounts'
    """

    # __connection__ = 'NAME'
    __table__ = "accounts"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []

    @has_many("uuid", "account_id")
    def wallets(self):
        from databases.models.wallets import WalletsModel

        return WalletsModel

    def get_transactions(self):
        from databases.models.transactions import TransactionsModel

        return TransactionsModel.where_in("from_id", self.wallets.pluck("uuid")).get()


AccountsModel.observe(AccountsObserver())
