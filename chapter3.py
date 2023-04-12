# resize and crop an image

import cv2

img = cv2.imread("assets/car.png")

# to find the shape of an image
print(img.shape)  # returns number of rows(height), columns(width), and channels(color:BGR)

# height,width,channels=img.shape
# print(height,width,channels)

# to resize an image

imgResize = cv2.resize(img, (200, 300))  # (400,300) width, height

cv2.imshow("retro car", img)
cv2.imshow("retro car resized", imgResize)

# croping a image
# using normal array slicing method
imgCroped = img[0:325, 200:425]  # height,width
cv2.imshow("retro car cropped", imgCroped)

cv2.waitKey(0)
