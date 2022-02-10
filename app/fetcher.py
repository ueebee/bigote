import os 
from dotenv import dotenv_values
from rich import print 
import asyncio
from binance import ThreadedWebsocketManager
from orator import DatabaseManager
from orator import Model
from models.mini_ticker import MiniTicker
from models.agg_trade import AggTrade
from models.depth import Depth
from loguru import logger
import time 

config = dotenv_values('.env')
logger.add(
    'logs/fetcher.ltsv',
    format="{time:YYYY-MM-DDTHH:mm:ss} \t{file} \t{name}:{function}:{line} \t{level} \t{message}",
    rotation='512 MB', retention=100
    )

def main():
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

    twm = ThreadedWebsocketManager(api_key=config['api_key'], api_secret=config['api_secret'])
    twm.start()

    def handle_socket_message(msg):
        # print(msg)
        try:
            if 'depth' in msg['stream']:
                depth = Depth()
                depth.save_data(msg)

            if 'miniTicker' in msg['stream']:
                mini_ticker = MiniTicker()
                mini_ticker.save_data(msg)
            
            if 'aggTrade' in msg['stream']:
                agg_trade = AggTrade()
                agg_trade.save_data(msg)
        except Exception as e:
            logger.error(e)

    streams = config['streams'].split(',')

    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)
    twm.join()

if __name__ == '__main__':
    main()

