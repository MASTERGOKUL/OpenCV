#CONVERTING normal Images to Gray Scale Images
import cv2
import numpy as np

img = cv2.imread("assets/dog.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert rgb to b&w
imgBlur = cv2.GaussianBlur(imgGray,(71,71),0)#(7,7) is blur ratio it must be in odd numbers#higher the sigma more the blur
imgCanny = cv2.Canny(img,100,100)#to get the edges of the image , thresh hold is selected to how sharp the edges

kernal = np.ones((5,5),np.uint8)
#kernal is a matrix contains all as 1
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)#to thick the edges for gapped/ not clear edges

imgEroded = cv2.erode(imgDialation,kernal,iterations=1)#oppostite of dilate it makes the edges thinner

cv2.imshow("original dog ",img)
cv2.imshow("gray dog ",imgGray)
cv2.imshow("blur dog ",imgBlur)
cv2.imshow("edge dog ",imgCanny)
cv2.imshow("dialation dog ",imgDialation)
cv2.imshow("eroded dog ",imgEroded)

cv2.waitKey(0)