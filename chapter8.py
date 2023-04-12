# contours / shape detection
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


def getContour(img):  # contour means getting shapes or detecting in cv2
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(contour, "contour")
    for cnt in contour:
        area = cv2.contourArea(cnt)
        print(area)
        # to draw our contours in an image
        if area > 500:  # we check it to avoid some noises like small objects
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0),
                             1)  # (image,contours,contourIndex(-1 because need to draw all points in a shape),color,thickness)
            peri = cv2.arcLength(cnt, True)  # (contour,closed or not)
            # print(peri)
            # to get the no of edges
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
            if objCor==3:
                text="Triangle"
            elif objCor==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05 :text="Square"
                else : text="Rectangle"
            elif objCor>4:
                text="Circle"
            cv2.putText(imgContour,text,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)



img = cv2.imread("assets/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)  # to get the edges

getContour(imgCanny)  # requires the edges i.e canny not the actual image

# cv2.imshow("shapes",img)
# cv2.imshow("Gray shapes",imgGray)
# cv2.imshow("Blur shapes",imgBlur)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgGray]))
cv2.imshow("stack", imgStack)
cv2.waitKey(0)
