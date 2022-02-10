from orator import Model


class AggTrade(Model):
    __table__ = 'agg_trades'
    __timestamps__ = False

    def save_data(self, msg):
        self.stream = msg['stream']
        self.e = msg['data']['e']
        self.E = msg['data']['E'] 
        self.s = msg['data']['s'] 
        self.a = msg['data']['a'] 
        self.p = msg['data']['p'] 
        self.q = msg['data']['q'] 
        self.f = msg['data']['f'] 
        self.l = msg['data']['l'] 
        self.T = msg['data']['T'] 
        self.m = msg['data']['m'] 
        self.M = msg['data']['M'] 
        self.save()




