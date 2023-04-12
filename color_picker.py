import cv2
import numpy as np
# a function to join the images
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def empty(a):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("color picker")
cv2.resizeWindow("color picker",500,500)
cv2.createTrackbar("Hue Minimum","color picker",0,179,empty)
cv2.createTrackbar("Hue Maximum","color picker",179,179,empty)
cv2.createTrackbar("Sat Minimum","color picker",0,255,empty)
cv2.createTrackbar("Sat Maximum","color picker",255,255,empty)
cv2.createTrackbar("Val Minimum","color picker",0,255,empty)
cv2.createTrackbar("Val Maximum","color picker",255,255,empty)
while True:
    success,img = cap.read()
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hue_min=cv2.getTrackbarPos("Hue Minimum","color picker")
    hue_max=cv2.getTrackbarPos("Hue Maximum","color picker")
    sat_min=cv2.getTrackbarPos("Sat Minimum","color picker")
    sat_max=cv2.getTrackbarPos("Sat Maximum","color picker")
    val_min=cv2.getTrackbarPos("Val Minimum","color picker")
    val_max=cv2.getTrackbarPos("Val Maximum","color picker")
    lower = np.array([hue_min,sat_min,val_min])
    higher = np.array([hue_max,sat_max,val_max])
    mask=cv2.inRange(imgHSV,lower,higher)
    imgResults=cv2.bitwise_and(img,img,mask=mask)
    stack = stackImages(0.5,([img,mask,imgResults]))
    cv2.imshow("img",stack)
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
