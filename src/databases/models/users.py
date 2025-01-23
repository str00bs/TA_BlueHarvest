"""
File contains users model
"""
from masoniteorm.models import Model
from masoniteorm.relationships import has_one
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin

from databases.observers.users import UsersObserver


class UsersModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """
    Database ORM Model for 'users'
    """

    # __connection__ = 'NAME'
    __table__ = "users"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []

    @has_one("uuid", "user_id")
    def preferences(self):
        from databases.models.preferences import PreferencesModel

        return PreferencesModel


UsersModel.observe(UsersObserver())
