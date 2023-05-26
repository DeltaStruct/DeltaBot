import os
import requests as api

class line:
    def __init__(self):
        self.api_key = os.environ["Line_Notify_API_Key"]
        self.api_send_url = f"https://notify-api.line.me/api/notify"
    
    def send(self, api_element):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'message': f'message: {api_element}'}
        requests.post(send.api_send_key, headers = headers, data = data)

def main():
    line.send("test")

if __name__ == "__main__":
    main()
