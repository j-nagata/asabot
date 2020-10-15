import os
import sys
import time
from asabotkit import qrauth, slackapi

try:
    client = slackapi.slackClient(token=os.environ['SLACK_BOT_TOKEN'])
    while (1):
        auth = qrauth.QRAuth()
        client.postFile(channel='general', file='auth.png')
        if auth.QRMonitoring():
            client.postChat(channel='general', message="認証成功")
        else:
            client.postChat(channel='general', message="認証失敗")

        time.sleep(2)

except KeyboardInterrupt:
    sys.exit()
finally:
    print('kill')
