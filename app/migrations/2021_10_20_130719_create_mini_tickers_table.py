from orator.migrations import Migration


class CreateMiniTickersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('mini_tickers') as table:
            table.big_increments('id')
            table.string('stream')
            table.string('e')
            table.big_integer('E')
            table.string('s')
            table.decimal('c', 32, 12)
            table.decimal('o', 32, 12)
            table.decimal('h', 32, 12)
            table.decimal('l', 32, 12)
            table.decimal('v', 32, 12)
            table.decimal('q', 32, 12)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('mini_tickers')
