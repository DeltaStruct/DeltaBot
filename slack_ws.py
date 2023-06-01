import os
import requests as api
import datetime
import sys

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
 
app = App(token=os.environ["Slack_BOT_API_Key"])
@app.message('test')
def test(message, say):
    time_now = datetime.datetime.now().strftime("%H時%M分%S秒")
    print("test\n現在時刻:" + time_now)
    say("test\n現在時刻:" + time_now)
def main():
    SocketModeHandler(app, os.environ["Slack_APP_API_Key"]).start()
if __name__ == "__main__":
    main()
    sys.exit(0)