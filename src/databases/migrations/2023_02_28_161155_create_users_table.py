"""CreateUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.uuid("uuid").primary()

            table.text("name", length=128)
            table.text("gender", length=32)
            table.integer("age", length=3)
            table.text("email", length=64)
            table.text("password", length=128, nullable=True)
            table.text("salt", length=128, nullable=True)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
