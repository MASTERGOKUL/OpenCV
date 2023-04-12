# chapter1- reading images,videos and webcam
import cv2

print("hi")

#read image using cv2.imread and display it using imshow,
#it disappears faster so use waitKey() ,
#waitKey(0) means infinite time

img = cv2.imread("assets/dog.png")
cv2.imshow("dogImage", img)
cv2.waitKey(1)

#to capture video use VideoCapture

cap = cv2.VideoCapture("assets/running_doggy.mp4")

#as we know video of running image we need to show it frame by frame in infinite loop
while True: #make it True
    success,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("running doggyyy",imgGray)
    # cv2.waitKey(200)#- also ok
    if cv2.waitKey(19) & 0xFF == ord('q'): #used to end the video while press q
        break

#to capture video from web cam

# cap = cv2.VideoCapture(0)#makes the computer cam to read vide0

#cap=cv2.VideoCapture("rtsp://10.10.177.116:8080/h264_ulaw.sdp")# while using ip cam #more delay
# cap = cv2.VideoCapture(0)#while using iv cam
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,500)
# while True: #make it True
#     success,img=cap.read()
#     cv2.imshow("running doggyyy",img)
#     # cv2.waitKey(200)#- also ok
#     if cv2.waitKey(19) & 0xFF == ord('q'): #used to end the video while press q
#         break