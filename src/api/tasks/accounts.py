"""File contains the AccountsTasks container"""

from api.schema.accounts import AccountsSchema


class AccountsTasks:
    """Tasks container for the AccountsRouter"""

    @staticmethod
    async def do_after(entity: AccountsSchema):
        print(f"Account.Name: {entity.name}")
