import cv2  # computervision
import RPi.GPIO as GPIO  # для светодиодов

GPIO.setmode(GPIO.BOARD)

cap = cv2.VideoCapture(0)  # нулевая-встроенная камера
face_detect = cv2.CascadeClassifier('facecascade.xml')  # переменная, принимающая путь до каскада лица

def FaceDetection(frame):
    status = False
    faces = face_detect.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5, minSize=(2, 2))  # принимаемое изображение границы

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (12, 255, 255), 1)
        status = True

    DoorStatus(status)
    return frame


def Handbreak():
    GPIO.setup(37, GPIO.OUT)

    str = input("Enter - on")
    if str != "":
        return 0
    else:
        GPIO.output(37, 1)
        Action()
    str = input("Enter - off")
    if str != "":
        return 0
    else:
        GPIO.output(37, 0)

    GPIO.cleanup(37)

def DoorStatus(status):
    GPIO.setup(7, GPIO.OUT)

    if status == True:
        GPIO.output(7, 1)
    else:
        GPIO.output(7, 0)
    GPIO.cleanup(7)

def Action():
    while True:

        ret, image = cap.read()  # считывает изображение

        output = FaceDetection(image)

        cv2.imshow('Camera', output)
        if cv2.waitKey(30) & 0xFF == 27:  # если будет нажата 27 кнопка(esc), то
            # break
            GPIO.output(37, 0)
            Handbreak()



def main():
    Handbreak()


if __name__ == "__main__":
    main()

GPIO.cleanup()

cap.release()
cv2.destroyAllWindows()
