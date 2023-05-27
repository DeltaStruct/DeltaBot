import os
import requests as api
from time import sleep
from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import line.py as line

class bybit_api:
    def __init__(self):
        self.api_key = os.environ["ByBit_API_Key"]
        self.secret = os.environ["ByBit_Secret_Key"]
        self.url = os.environ["ByBit_url"]
        self.ws = WebSocket(
          test = True,
          api_key = self.api_key,
          api_secret = self.api_secret
        )
    
    def get_info(self):
        
