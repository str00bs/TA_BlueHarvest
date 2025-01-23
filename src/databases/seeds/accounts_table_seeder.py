"""File contains seeder for the 'accounts' table"""

from random import choice
from secrets import token_urlsafe
from uuid import uuid4

from faker import Faker
from masoniteorm.seeds import Seeder

from api.schema.accounts import AccountsSchema
from databases.models import AccountsModel


class AccountsTableSeeder(Seeder):
    """Seeder for the 'accounts' table"""

    def run(self):
        """Run the database seeds."""
        for account in range(1, 3):
            # ? Create Fake data
            fake = Faker()
            account_id = uuid4()
            fake_first_name = fake.first_name()
            fake_last_name = fake.last_name()
            fake_age = fake.random_int(min=25, max=55)
            fake_email = (
                f"{fake_first_name.lower()}_{fake_last_name.lower()}"
                f"{fake_age}@example.com"
            )

            # ? Fill-in schema
            account_schema = AccountsSchema(
                uuid=account_id,
                first_name=fake_first_name,
                last_name=fake_last_name,
                age=fake_age,
                email=fake_email,
                initial_balance=fake.pydecimal(
                    min_value=1,
                    max_value=1000,
                    positive=True,
                    right_digits=2,
                ),
                is_anonymous=False,
                password=token_urlsafe(16),
                salt=token_urlsafe(128),
                type_=choice(["customer", "admin"]),
            )
            secrets = account_schema.get_secrets()
            account = account_schema.model_dump()
            account.update(secrets)

            # ? Create records
            AccountsModel.create(account)
