import cv2
import time
import string
import random
import qrcode
import PIL


class QRAuth:
    def __init__(self, path='auth.png'):
        self.auth = self.issueAuth()
        self.path = path
        self.issueQRCode(self.auth, self.path)

    def QRMonitoring(self):
        cap = cv2.VideoCapture(0)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))

        while (cap.isOpened()):
            ret, frame = cap.read()

            result = self.isSucceeded(frame)
            if result is not None:
                cap.release()
                return result

            time.sleep(0.1)

    def isSucceeded(self, img):
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)
        if data != '':
            return data == self.auth
        return None

    def issueQRCode(self, auth, path):
        qrimg = qrcode.make(auth)
        qrimg.save(path)

    def issueAuth(self, length=30):
        return ''.join([random.choice(string.punctuation + string.ascii_letters + string.digits) for i in range(length)])
