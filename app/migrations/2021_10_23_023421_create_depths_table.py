from orator.migrations import Migration


class CreateDepthsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('depths') as table:
            table.big_increments('id')
            table.string('stream')
            table.big_integer('last_update_id')
            table.json('bids_asks')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('depths')
