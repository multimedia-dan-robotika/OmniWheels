import numpy as np
import cv2

# if camera not found, please check this scirpt and change 0 parameter to 1
cam = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

id = input('Enter User id : ')
sampleNum = 0
while True:
    Cball = 0
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum+1
        cv2.imwrite("dataset/User."+str(id)+"." +
                    str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.waitKey(100)
        cv2.imshow("face", img)
        cv2.waitKey(1)
        # Sample pengambilan data
    if (sampleNum >= 100):
        print("Finished!")
        break

cam.release()
cv2.destroyAllWindows()
