import os
import requests as api
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class slack_api:
    def __init__(self):
        #アプリの初期化
        self.app = App(token=os.environ['Slack_BOT_API_Key'])
        SocketModeHandler(app, os.environ['Slack_APP_API_Key']).start()
    def test(self):
        time_now = datetime.datetime.now().strftime("%H時%M分%S秒")
        say("test\n現在時刻" + time_now)
    def send(self, mes):
        say(mes)
if __name__ == "__main__":
  slack = slack_api()
  slack.test()