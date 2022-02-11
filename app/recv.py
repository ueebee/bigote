from locale import currency
import os 
from dotenv import dotenv_values
from rich import print 
import asyncio
from orator import DatabaseManager
from orator import Model
from models.mini_ticker import MiniTicker
from models.agg_trade import AggTrade
from models.depth import Depth
from models.currency_pair_log import CurrencyPairLog
from loguru import logger
import time 
from fastapi import FastAPI
from models.currency_pair import CurrencyPair

config = dotenv_values('.env')
logger.add(
    'logs/recv.ltsv',
    format="{time:YYYY-MM-DDTHH:mm:ss} \t{file} \t{name}:{function}:{line} \t{level} \t{message}",
    rotation='512 MB', retention=100
    )

db_config = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': config['db_host'],
        'database': config['db_name'],
        'user': config['db_user'],
        'password': config['db_pass'],
        'prefix': ''
    }
}
db = DatabaseManager(db_config)
Model.set_connection_resolver(db)
app = FastAPI()

@app.get("/")
async def hello():
    return {"message" : "Hello,World"}

@app.post("/currency_pair")
async def create_currency_pair(currency_pair: CurrencyPair):
    msg = currency_pair.to_msg()
    cpl = CurrencyPairLog()
    cpl.save_data(msg)
    return {'res': 'ok', 'name': currency_pair.name, 'bid': currency_pair.bid, 'ask': currency_pair.ask}
