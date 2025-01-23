"""File contains 'users' model observer"""
import hashlib
from uuid import uuid4

from masoniteorm.models import Model

from databases.models.preferences import PreferencesModel


class UsersObserver:
    def created(self, user: Model):
        """
        Handle the Users "created" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        print("User created")
        # ? Add preferences
        PreferencesModel.create({"uuid": uuid4(), "user_id": user.uuid})
        return user

    def creating(self, user: Model):
        """
        Handle the Users "creating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        # ? Hash password
        hasher = hashlib.new("sha512")
        hasher.update(f"{user.password}{user.salt}".encode("utf-8"))
        user.password = hasher.hexdigest()
        user.save()
        return user.fresh()

    def saving(self, user: Model):
        """
        Handle the Users "saving" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def saved(self, user: Model):
        """
        Handle the Users "saved" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def updating(self, user: Model):
        """
        Handle the Users "updating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def updated(self, user: Model):
        """
        Handle the Users "updated" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def booted(self, user: Model):
        """
        Handle the Users "booted" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        return user

    def booting(self, user: Model):
        """
        Handle the Users "booting" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrating(self, user: Model):
        """
        Handle the Users "hydrating" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrated(self, user: Model):
        """
        Handle the Users "hydrated" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def deleting(self, user: Model):
        """
        Handle the Users "deleting" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass

    def deleted(self, user: Model):
        """
        Handle the Users "deleted" event.

        Args:
            user (masoniteorm.models.Model): Users model.
        """
        pass
