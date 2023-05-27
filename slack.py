import os
import requests as api
import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class slack_api:
    def __init__(self):
        self.app = App(token=os.environ["Slack_BOT_API_Key"])
        print(2)
        SocketModeHandler(self.app, os.environ["Slack_APP_API_Key"]).start()
    def test(self):
        time_now = datetime.datetime.now().strftime("%H時%M分%S秒")
        print(4)
        say("test\n現在時刻:" + time_now)
    def send(self, msg):
        say(msg)
def main():
    print(1)
    slack = slack_api()
    print(3)
    slack.test()
    print(5)
    sys.exit(0)
if __name__ == "__main__":
    main()
    sys.exit(0)
