#face detection - viola and jons method
import cv2

cap= cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
while True:
    success,img=cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(imgGray,1.1,4)
    print(face)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        print(x,y,w,h)
    cv2.imshow("detected",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
