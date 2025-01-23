"""CreateWalletsTable Migration."""

from masoniteorm.migrations import Migration


class CreateWalletsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wallets") as table:
            table.uuid("uuid").primary()
            table.decimal("balance", 17, 2).default(0.0)

            table.uuid("account_id").foreign("account_id").references("uuid").on(
                "accounts"
            ).on_delete("cascade")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("Wallets")
