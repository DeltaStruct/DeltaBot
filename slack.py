import os
import requests as api

import os
from slack_sdk.web import WebClient
class slack_api:
    def __init__(self):
        self.client = WebClient(token=os.environ["Slack_BOT_API_Key"])
    def test(self):
        self.response = self.client.chat_postMessage(text=":wave: こんにちは！", channel="#random")
        print(self.response)
def main():
    slack = slack_api()
    slack.test()
    sys.exit(0)
if __name__ == "__main__":
    main()
    sys.exit(0)
