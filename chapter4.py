# creating shapes and texts on images
import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)  # as we know image is a 2d matrix of colors, here 0 means black color

# img[:]=250,250,34 # [[[250 250   3] -> this assigns each row as given value
# img[200:300,300:400]=250,250,34 #  -> this assigns each row as given value for the given range

# draw a line in image
cv2.line(img, (0, 0), (500, 500), (0, 255, 0), 5)  # (image,startingpoint,endingpoint,color,thickness)
# note color combination here is BGR not RGB
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0),
#          5)  # can also use dimension note that:.shape gives height
# and width but points needs width and height i.e x and y

#draw a rectangle

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 3)  # same syntax as line
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)  # to fill the area use this cv2.FILLED instead of thickness
cv2.circle(img,(125,175),150,(255,255,34),cv2.FILLED)#(image,center_point,radius,color,thickness)

#draw a circle


#drawing of national flag
# img2=np.zeros((300,500,3),np.uint8)
# cv2.rectangle(img2,(0,0),(500,100),(0,165,255),cv2.FILLED)
# cv2.rectangle(img2,(0,100),(500,200),(255,255,255),cv2.FILLED)
# cv2.rectangle(img2,(0,200),(500,300),(32,50,1),cv2.FILLED)
# cv2.circle(img2,(250,150),50,(200,0,0),cv2.FILLED)

#write a text in the image
cv2.putText(img,"GOKUL",(50,200),cv2.FONT_HERSHEY_COMPLEX,4,(10,203,203),3) #(image,text,origin,fontStyle,fontHeight,color,thickness)



cv2.imshow("np image", img)
# cv2.imshow("indian flag", img2)
cv2.waitKey(0)
