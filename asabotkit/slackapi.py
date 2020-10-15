import os
from slack import WebClient
from slack.errors import SlackApiError


class slackClient:

    def __init__(self, token):
        self.client = WebClient(token)

    def postChat(self, channel, message):
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=message
            )
            assert response['message']['text'] == message
        except SlackApiError as e:
            assert e.response['ok'] is False
            assert e.response['error']
            print(f"Got an error: {e.response['error']}")

    def postFile(self, channel, file, title=None):
        try:
            response = self.client.files_upload(
                channels=channel,
                file=file,
                title=title
            )
            assert response['file']
        except SlackApiError as e:
            assert e.response['ok'] is False
            assert e.response['error']
            print(f"Got an error: {e.response['error']}")
