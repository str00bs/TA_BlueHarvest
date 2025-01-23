"""File contains 'wallets' model observer"""

from uuid import uuid4

from masoniteorm.models import Model

from databases.models.transactions import TransactionsModel


class WalletsObserver:
    def created(self, wallet: Model):
        """
        Handle the Wallets "created" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        # ? Add transaction if initial balance is not 0
        if wallet.balance != 0:
            TransactionsModel.create(
                {
                    "uuid": uuid4(),
                    "from_id": wallet.uuid,
                    "to_id": wallet.uuid,
                    "amount": wallet.balance,
                    "description": "Initial balance",
                }
            )
        return wallet

    def creating(self, wallet: Model):
        """
        Handle the Wallets "creating" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def saving(self, wallet: Model):
        """
        Handle the Wallets "saving" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def saved(self, wallet: Model):
        """
        Handle the Wallets "saved" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def updating(self, wallet: Model):
        """
        Handle the Wallets "updating" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def updated(self, wallet: Model):
        """
        Handle the Wallets "updated" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def booted(self, wallet: Model):
        """
        Handle the Wallets "booted" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        return wallet

    def booting(self, wallet: Model):
        """
        Handle the Wallets "booting" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def hydrating(self, wallet: Model):
        """
        Handle the Wallets "hydrating" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def hydrated(self, wallet: Model):
        """
        Handle the Wallets "hydrated" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def deleting(self, wallet: Model):
        """
        Handle the Wallets "deleting" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass

    def deleted(self, wallet: Model):
        """
        Handle the Wallets "deleted" event.

        Args:
            wallet (masoniteorm.models.Model): Wallets model.
        """
        pass
