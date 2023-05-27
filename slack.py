import os
import requests as api
import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class slack_api:
    def __init__(self):
        self.app = App(token=os.environ["Slack_BOT_API_Key"])
        SocketModeHandler(self.app, os.environ["Slack_APP_API_Key"]).start()
    def test(self):
        time_now = datetime.datetime.now().strftime("%H時%M分%S秒")
        say("test\n現在時刻:" + time_now)
    def send(self, msg):
        say(msg)
def main():
    slack = slack_api()
    slack.test()
    sys.exit(0)
if __name__ == "__main__":
    main()
    sys.exit(0)
