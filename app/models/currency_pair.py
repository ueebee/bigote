from pydantic import BaseModel


class CurrencyPair(BaseModel):
    name: str
    time: int
    bid: float 
    ask: float
    last: float
    volume: float
    time_msc: int

    def to_msg(self):
        msg = {
            'name': self.name,
            'time': self.time,
            'bid': self.bid,
            'ask': self.ask,
            'last': self.last,
            'volume': self.volume,
            'time_msc': self.time_msc,
        }
        return msg
