import cv2
import numpy as np
#a function to join the images
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def empty(a):
    pass
img=cv2.imread("assets/car.png")
cv2.namedWindow("TrackWindow")
cv2.resizeWindow("TrackWindow",600,400)
#initial stage
# cv2.createTrackbar("Hue Min","TrackWindow",0,179,empty)#(trackbarname,window name, starting,ending,onchangeFunction)
# cv2.createTrackbar("Hue Max","TrackWindow",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackWindow",0,255,empty)
# cv2.createTrackbar("Sat Max","TrackWindow",255,255,empty)
# cv2.createTrackbar("Val Min","TrackWindow",0,255,empty)
# cv2.createTrackbar("Val Max","TrackWindow",255,255,empty)

#after knowing the HSV for the color
cv2.createTrackbar("Hue Min","TrackWindow",37,179,empty)#(trackbarname,window name, starting,ending,onchangeFunction)
cv2.createTrackbar("Hue Max","TrackWindow",114,179,empty)
cv2.createTrackbar("Sat Min","TrackWindow",48,255,empty)
cv2.createTrackbar("Sat Max","TrackWindow",237,255,empty)
cv2.createTrackbar("Val Min","TrackWindow",55,255,empty)
cv2.createTrackbar("Val Max","TrackWindow",200,255,empty)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#convert color to HSV
while True:
    h_min=cv2.getTrackbarPos("Hue Min","TrackWindow")
    h_max=cv2.getTrackbarPos("Hue Max","TrackWindow")
    s_min=cv2.getTrackbarPos("Sat Min","TrackWindow")
    s_max=cv2.getTrackbarPos("Sat Max","TrackWindow")
    v_min=cv2.getTrackbarPos("Val Min","TrackWindow")
    v_max=cv2.getTrackbarPos("Val Max","TrackWindow")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    #to get mask of an image for specific color
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResults=cv2.bitwise_and(img,img,mask=mask)#to merge two image

    # cv2.imshow("car",img)
    # cv2.imshow("car HSV",imgHSV)
    # cv2.imshow("car Mask",mask)
    # cv2.imshow("image results",imgResults)
    imgStack = stackImages(0.8,([img,imgHSV],[mask,imgResults]))
    cv2.imshow("Stack results",imgStack)
    cv2.waitKey(1)