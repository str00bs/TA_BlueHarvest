"""CreateAccountsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("accounts") as table:
            table.uuid("uuid").primary()

            table.enum("type_", ["customer", "admin"])
            table.boolean("is_anonymous").default(False)

            table.text("first_name", length=128)
            table.text("last_name", length=128)
            table.integer("age", length=3)
            table.text("email", length=64)
            table.decimal("initial_balance", 17, 2).default(0.0)
            table.text("password", length=128, nullable=True)
            table.text("salt", length=128, nullable=True)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("accounts")
