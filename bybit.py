# -*- coding: utf-8 -*-
import os
import requests as api
from time import sleep
from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import line
import slack

class bybit_api:
    def tickers_callback(self, message:"入力") -> "ティッカーWebSocketのコールバック関数":
        self.price = float(message["data"]["lastPrice"])
    
    def trade_coin(self, coin_target:"string 取引対象", coin_source:"string 取引元") -> "取引パターンを設定":
        self.coin_pattern = str(coin_target) + str(coin_source)
        
    def __init__(self, coin_target:"string 取引対象", coin_source:"string 取引元", is_test:"bool テストネットを使用するか"):
        self.envtest = ""
        if is_test:
            self.envtest = "Testnet_"
        self.api_key = os.environ[self.envtest+"ByBit_API_Key"]
        self.api_secret = os.environ[self.envtest+"ByBit_Secret_Key"]
        # WebSocketなんか国がブロックされてる。アメリカを？？？
        self.session = HTTP(
            # HTTP requests
            testnet = is_test,
            api_key = self.api_key,
            api_secret = self.api_secret,
        )
        self.coin_pattern = ""
        self.trade_coin(coin_target, coin_source)
        self.price = 0
    def get_tickers(self):
        res = session.get_tickers(
            category="inverse",
            symbol="BTCUSD",
        )
        return res

if __name__ == "__main__":
    bybit = bybit_api("ETH", "USDT", True)
    slack = slack.http("#random")
    slack.send("こんにちは！これちゃんとさぶみっとできてるかな〜")
    slack.send(bybit.get_tickers()["result"]["list"][0][0]["lastPrice"])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
