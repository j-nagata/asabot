import os
import time
from slack import WebClient
from slack.errors import SlackApiError
from asabotkit import qrauth

token = os.environ['SLACK_BOT_TOKEN']
client = WebClient(token=token)

def issueNewAuthQR(auth):
    qrauth.QRImage(auth=auth, path='auth.png')
    response = client.files_upload(
        channels='creating-bot-project',
        file='auth.png',
        title='認証QRコード'
    )

try:
    while (1):
        auth = qrauth.IssueAuth()
        issueNewAuthQR(auth)
        
        while (auth != qrauth.QRMonitoring()):
            response = client.chat_postMessage(
                channel='creating-bot-project',
                text='QRコードが異なります'
            )
            assert response['message']['text'] == 'QRコードが異なります'

        response = client.chat_postMessage(
            channel='creating-bot-project',
            text='認証成功!'
        )
        assert response['message']['text'] == '認証成功!'

        time.sleep(2)

except SlackApiError as e:
    assert e.response['ok'] is False
    assert e.response['error']
    print(f"Got an error: {e.response['error']}")
