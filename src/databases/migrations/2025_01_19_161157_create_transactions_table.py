"""CreateTransactionsTable Migration."""

from masoniteorm.migrations import Migration


class CreateTransactionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("transactions") as table:
            table.uuid("uuid").primary()
            table.decimal("amount", 17, 2).default(0.0)
            table.text("description", length=255, nullable=True)
            table.uuid("from_id").foreign("from_id").references("uuid").on("wallets")
            table.uuid("to_id").foreign("to_id").references("uuid").on("wallets")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("Transactions")
