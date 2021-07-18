import cv2
import datetime

plate_classifier = cv2.CascadeClassifier("haarcascade_licence_plate_rus_16stages.xml")
eye_classifier = cv2.CascadeClassifier("haarcascade_eye.xml")
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
car_classifier = cv2.CascadeClassifier("haarcascade_car.xml")


img=cv2.imread("boys.jpg")
grcp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plates = plate_classifier.detectMultiScale(grcp, 1.1, 5)
eyes = eye_classifier.detectMultiScale(grcp,1.3,5)
faces = face_classifier.detectMultiScale(grcp,1.3,5)
cars = car_classifier.detectMultiScale(grcp,1.3,5)

for pl1,pl2,pl3,pl4 in plates: 
    cv2.rectangle(img, (pl1,pl2), (pl1+pl3,pl2+pl4), (0,0,255), 5)
    cv2.putText(img, 'plate', (pl1-10,pl2-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        
for(ey1,ey2,ey3,ey4) in eyes:
    cv2.rectangle(img, (ey1,ey2), (ey1+ey3,ey2+ey4), (0,0,255), 2)
    cv2.putText(img, 'Eyes', (ey1,ey2-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 1)
    
for(fa1,fa2,fa3,fa4) in faces:
    cv2.rectangle(img, (fa1,fa2), (fa1+fa3,fa2+fa4), (0,0,255), 2)
    cv2.putText(img, 'Face', (fa1,fa2-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 3)
    
##for(ca1,ca2,ca3,ca4) in cars:
##    cv2.rectangle(img, (ca1,ca2), (ca1+ca3,ca2+ca4), (0,0,255), 2)
##    cv2.putText(img, 'Car', (ca1,ca2-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 3)
##
    
cv2.imshow('image', img)
