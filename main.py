#for install libraries    pip install --force-reinstall --no-cache -U opencv-python==4.5.5.62
#where to download cascades (for the future)   https://github.com/opencv/opencv/tree/4.x/data/haarcascades
import cv2


cap = cv2.VideoCapture(0)
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

def PersonDetection(frame):
    status = False
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (humans, _) = hog.detectMultiScale(frame, winStride=(5, 5), padding=(3, 3), scale=1.21)

    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        status = True

    DoorStatus(status)
    return frame


def DoorStatus(status):

    if status == True:
        print("True")
    else:
        print("False")

def main():
    while True:
        ret, img = cap.read()

        if ret:
            output = PersonDetection(img)

            cv2.imshow("Camera", output)



            exit = cv2.waitKey(30) & 0xFF
            if exit == 27:  # esc push to exit
                break
        else:
            print("UPS i dead...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


