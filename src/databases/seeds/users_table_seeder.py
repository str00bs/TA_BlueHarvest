"""File contains seeder for the 'users' table"""
from secrets import token_urlsafe
from random import choice

from masoniteorm.seeds import Seeder
from faker import Faker

from databases.models import UsersModel
from api.schema.users import UsersSchema


class UsersTableSeeder(Seeder):
    """Seeder for the 'users' table"""

    def run(self):
        """Run the database seeds."""
        for user in range(1, 10):
            fake = Faker()
            fake_age = fake.random_int(min=25, max=55)
            fake_name = fake.name()
            fake_email = f"{fake_name.lower().replace(' ', '_')}{fake_age}@example.com"

            UsersModel.create(UsersSchema(
                name=fake_name,
                age=fake_age,
                email=fake_email,
                gender=choice(["Male", "Female", "Nonbinary"]),
                password=token_urlsafe(16),
                salt=token_urlsafe(128)
            ).model_dump())
