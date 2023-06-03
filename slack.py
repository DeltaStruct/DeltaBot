import os
import requests as api
import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web import WebClient as Web_Slack
 
app = App(token=os.environ["Slack_BOT_API_Key"])
@app.message('test')
def test(message, say):
    time_now = datetime.datetime.now().strftime("%H時%M分%S秒")
    print("test\n現在時刻:" + time_now)
    say("test\n現在時刻:" + time_now)
def main():
    SocketModeHandler(app, os.environ["Slack_APP_API_Key"]).start()

class http:
    def __init__(self, ch:"string"):
        self.ch = str(ch)
        self.client = Web_Slack(token=os.environ["Slack_BOT_API_Key"])
    
    def send(self, msg:"string"):
        self.rensponse = self.client.chat_postMessage(text=msg, channel=self.ch)
        print("slack_api msg: ", msg, ' ', self.rensponse)
        
if __name__ == "__main__":
    main()
