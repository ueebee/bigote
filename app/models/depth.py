from orator import Model
from orator.orm import scope
import json

class Depth(Model):
    __table__ = 'depths'
    __timestamps__ = False

    def save_data(self, msg):
        json_msg = json.dumps(msg['data'])
        # print(json_msg)
        self.stream = msg['stream']
        self.last_update_id = msg['data']['lastUpdateId']
        self.bids_asks = json_msg
        # self.bids_asks = msg
        self.save()

    @scope 
    def last(self, query):
        return query.order_by('id', 'desc')

    # def last(self):
        


