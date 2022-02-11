from orator.migrations import Migration


class CreateCurrencyPairLogs(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('currency_pair_logs') as table:
            table.big_increments('id')
            table.string('name')
            table.big_integer('time')
            table.decimal('bid', 32, 12)
            table.decimal('ask', 32, 12)
            table.decimal('last', 32,12)
            table.decimal('volume', 32,12)
            table.big_integer('time_msc')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('currency_pair_logs')
