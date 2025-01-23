"""
File contains preferences model
"""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import UUIDPrimaryKeyMixin


class PreferencesModel(Model, UUIDPrimaryKeyMixin):
    """
    Database ORM Model for 'preferences'
    """

    # __connection__ = 'NAME'
    __table__ = "preferences"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    # __hidden__ = []

    @belongs_to("user_id", "uuid")
    def user(self):
        from databases.models.users import UsersModel

        return UsersModel
