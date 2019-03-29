
#import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:\\Maestria\\Reconocimiento de patrones\\OpenCV\\Detector de sonrisa\\data_haarcascade\\haarcascade_frontalface_alt.xml')
smile_cascade= cv2.CascadeClassifier('D:\\Maestria\\Reconocimiento de patrones\\OpenCV\\Detector de sonrisa\\data_haarcascade\\haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('D:\\Maestria\\Reconocimiento de patrones\\OpenCV\\Detector de sonrisa\\data_haarcascade\\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    global X
    global Y
    ###Face detection
    for (x, y, w, h) in faces:
        
        X=x
        Y=y
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        ###smile detection
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        ##Eye Detection
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            print ("ojos"), len(eyes), ("eyes!")

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            print ("sonrisa"), len(smile), ("smiles!")
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(img,'Feliz..!',(X+50,Y+200),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255),1,cv2.LINE_AA)


    cv2.putText(img,'Balzhoyt',(X,Y),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,0,255),1,cv2.LINE_AA)
    cv2.imshow('Face', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()