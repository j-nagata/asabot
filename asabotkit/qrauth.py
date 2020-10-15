import cv2
import time
import string
import random
import qrcode
import PIL

def QRMonitoring():

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))

    detector = cv2.QRCodeDetector()

    while (cap.isOpened()):
        ret, frame = cap.read()
        data, points, _ = detector.detectAndDecode(frame)

        if data != '':
            print('data: ', data)
            return data

        time.sleep(0.07)

def QRImage(auth, path):
    qrimg = qrcode.make(auth)
    qrimg.save(path)

def IssueAuth():
    auth = ''.join([random.choice(string.punctuation + string.ascii_letters + string.digits) for i in range(30)])
    return auth