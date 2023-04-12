# warp perspective
import cv2
import numpy as np

img = cv2.imread("assets/cards.png")
width, height = 220, 300
pts1 = np.float32([[490, 140], [710, 81], [523, 442],[773, 386]])#1)top-left 2)top-right 3)bottom-left 4)bottom-right
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])#output screen  width
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("wrap cards", img)
cv2.imshow("wrap cards 2", imgOutput)

demoImg=cv2.imread("assets/cards2.png")
ptns1=np.float32([[172,229],[238,229],[182,321],[269,319]])
m=cv2.getPerspectiveTransform(ptns1,pts2)
cardout=cv2.warpPerspective(demoImg,m,(width,height))
cv2.imshow("complex image warp",cardout)
cv2.imshow("complex image",demoImg)
cv2.waitKey(0)
