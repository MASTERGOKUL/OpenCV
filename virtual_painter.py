import cv2
import numpy as np
frameWidth = 1080
frameHeight = 2000
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[5,107,0,19,255,255],#the hsv you want for a color
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



while True:
    success, img = cap.read()
    imgResult = img.copy()

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("paint.png",imgResult)
        break