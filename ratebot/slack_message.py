import json
import os
import requests


class SlackMessage:
    def __init__(self):
        self.webhook_url = os.environ['SLACK_WEBHOOK_URL']

    def send_message(self, text):
        message = {'text': text}
        response = requests.post(
            self.webhook_url,
            data=json.dumps(message),
            headers={'Content-Type': 'application/json'}
        )
