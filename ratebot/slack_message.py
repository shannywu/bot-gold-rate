import json
import requests


class SlackMessage:
    def __init__(self):
        self.webhook_url = 'https://hooks.slack.com/services/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'

    def send_message(self, text):
        message = {'text': text}
        response = requests.post(
            self.webhook_url,
            data=json.dumps(message),
            headers={'Content-Type': 'application/json'}
        )
