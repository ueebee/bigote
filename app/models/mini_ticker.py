from orator import Model

class MiniTicker(Model):
    __table__ = 'mini_tickers'
    # __guarded__ = ['*']
    __timestamps__ = False

    def save_data(self, msg):
        self.stream = msg['stream']
        self.e = msg['data']['e']
        self.E = msg['data']['E']
        self.s = msg['data']['s']
        self.c = msg['data']['c']
        self.o = msg['data']['o']
        self.h = msg['data']['h']
        self.l = msg['data']['l']
        self.v = msg['data']['v']
        self.q = msg['data']['q']
        self.save()
        
