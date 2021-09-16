import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
censuredPng = cv2.imread("img/censured.png")

while True:
    success, img = cap.read()
    img2 = img
    success, img = cap.read()
    img = cv2.flip(img,1)
    img2 = cv2.flip(img2,1)

    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    h,w, _ = censuredPng.shape

    if lmList:
        middleFinger, _, line = detector.findDistance(9,12,img)
        indexFinger,_,_ = detector.findDistance(5,8,img)
        ringFinger,_,_ = detector.findDistance(13,16,img)
        if middleFinger > 70 and indexFinger< 120 and ringFinger < 120:
            img[ line[3]: line[3] + h,  line[2] - 202: line[2] + 202] = censuredPng
            img2[ line[3]: line[3] + h,  line[2] - 202: line[2] + 202] = censuredPng
        cursor = lmList[8]

    cv2.imshow("image", img)
    cv2.imshow("image2", img2)

    cv2.waitKey(1)