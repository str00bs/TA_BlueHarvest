"""File contains 'accounts' model observer"""

import hashlib
from uuid import uuid4

from masoniteorm.models import Model

from databases.models.wallets import WalletsModel


class AccountsObserver:
    def created(self, account: Model):
        """
        Handle the Accounts "created" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        # ? Add wallets
        WalletsModel.create(
            {
                "uuid": uuid4(),
                "account_id": account.uuid,
                "balance": account.initial_balance,
            }
        )
        return account

    def creating(self, account: Model):
        """
        Handle the Accounts "creating" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        # ? Hash password
        hasher = hashlib.new("sha512")
        hasher.update(f"{account.password}{account.salt}".encode("utf-8"))
        account.password = hasher.hexdigest()
        account.save()
        return account.fresh()

    def saving(self, account: Model):
        """
        Handle the Accounts "saving" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def saved(self, account: Model):
        """
        Handle the Accounts "saved" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def updating(self, account: Model):
        """
        Handle the Accounts "updating" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def updated(self, account: Model):
        """
        Handle the Accounts "updated" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def booted(self, account: Model):
        """
        Handle the Accounts "booted" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        return account

    def booting(self, account: Model):
        """
        Handle the Accounts "booting" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def hydrating(self, account: Model):
        """
        Handle the Accounts "hydrating" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def hydrated(self, account: Model):
        """
        Handle the Accounts "hydrated" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def deleting(self, account: Model):
        """
        Handle the Accounts "deleting" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass

    def deleted(self, account: Model):
        """
        Handle the Accounts "deleted" event.

        Args:
            account (masoniteorm.models.Model): Accounts model.
        """
        pass
