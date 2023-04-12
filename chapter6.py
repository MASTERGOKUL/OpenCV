#joining images
import cv2
import numpy as np
img = cv2.imread("assets/dog.png")
imgHor=np.hstack((img,img))#it is a numpy fucntion to merge images horizontally
imgVer=np.vstack((img,img,img))#it is a numpy fucntion to merge images vertically
# imgVer=np.vstack((imgHor,imgHor,imgHor))#to make a square 
cv2.imshow("horizontal",imgHor)
cv2.imshow("vertical",imgVer)
cv2.waitKey(0)