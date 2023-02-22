#библиотеки pip install --force-reinstall --no-cache -U opencv-python==4.5.5.62
#каскады https://github.com/opencv/opencv/tree/4.x/data/haarcascades

import numpy as np #для массивов
import cv2 #computervision

cap = cv2.VideoCapture(0) #нулевая-встроенная камера
face_detect = cv2.CascadeClassifier('facecascade.xml') #переменная, принимающая путь до каскада лица
#body_detect = cv2.CascadeClassifier('haarcascade_fullbody.xml') #переменная, принимающая путь до каскада тела

while (True):
    ret, image = cap.read() #считывает изображение
    faces = face_detect.detectMultiScale(image, scaleFactor=1.5, minNeighbors=5, minSize=(2, 2)) #принимаемое изображение границы
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (12, 255, 255), 1)
    cv2.imshow('Camera', image)
    if cv2.waitKey(30) & 0xFF == 27:
        break #если будет нажата 27 кнопка(esc), то выход программы

#while (True):
 #   ret, image = cap.read()  # считывает изображение
  #  faces = body_detect.detectMultiScale(image, scaleFactor=1.5, minNeighbors=5, minSize=(10, 10))  # принимаемое изображение границы
   # for (x, y, w, h) in faces:
    #    cv2.rectangle(image, (x, y), (x + w, y + h), (12, 0, 56), 1)
    #cv2.imshow('Camera', image)
    #if cv2.waitKey(30) & 0xFF == 27:
    #    break  # если будет нажата 27 кнопка(esc), то выход программы

cap.release()
cv2.destroyAllWindows()