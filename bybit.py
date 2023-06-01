# -*- coding: utf-8 -*-
import os
import requests as api
from time import sleep
from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import line
#import slack_http as slack

class bybit_api:
    def __init__(self, coin_target, coin_source, is_test):
        # coin_target string
        # coin_source string
        # is_test bool
        if is_test:
            # testnet mode
            self.api_key = os.environ["Testnet_ByBit_API_Key"]
            self.secret = os.environ["Testnet_ByBit_Secret_Key"]
        else :
            # realnet mode
            self.api_key = os.environ["ByBit_API_Key"]
            self.api_secret = os.environ["ByBit_Secret_Key"]
        self.ws = WebSocket(
          # websocket requests
          test = is_test,
          api_key = self.api_key,
          api_secret = self.api_secret
        )
        self.session = HTTP(
            # HTTP requests
            test = is_test,
            api_key = self.api_key,m
            api_secret = self.api_secret
        )
        self.coin_pattern = ""
        trade_coin(coin_terget, coin_source)
        self.price = 0
    
    def tickers_callback(self, message):
        self.price = float(message["data"]["lastPrice"])
    
    def trade_coin(self, coin_target, coin_source):
        # coin_target string トレード対象
        # coin_source string トレード元
        self.coin_pattern = coin_target + coin_source
    
    def order_buy(self, usd):
