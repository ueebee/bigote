from orator.migrations import Migration


class CreateAggTradesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('agg_trades') as table:
            table.big_increments('id')
            table.string('stream')
            table.string('e')
            table.big_integer('E')
            table.string('s')
            table.big_integer('a')
            table.decimal('p', 32, 12)
            table.decimal('q', 32, 12)
            table.big_integer('f')
            table.big_integer('l')
            table.big_integer('T')
            table.boolean('m')
            table.boolean('M')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('agg_trades')

