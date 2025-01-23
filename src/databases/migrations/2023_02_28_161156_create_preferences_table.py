"""CreatePreferencesTable Migration."""

from masoniteorm.migrations import Migration


class CreatePreferencesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("preferences") as table:
            table.uuid("uuid").primary()
            table.boolean("toggle_dark_mode").default(True)
            table.boolean("toggle_email").default(True)
            table.boolean("toggle_notifications").default(True)

            table.uuid("user_id").foreign("user_id").references("uuid").on(
                "users"
            ).on_delete("cascade")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("preferences")
