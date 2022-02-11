from orator import Model

class CurrencyPairLog(Model):
    __table__ = 'currency_pair_logs'
    __timestamps__ = False

    def save_data(self, msg):
        self.name = msg['name']
        self.time = msg['time']
        self.bid = msg['bid']
        self.ask = msg['ask']
        self.last = msg['last']
        self.volume = msg['volume']
        self.time_msc = msg['time_msc']
        self.save()
