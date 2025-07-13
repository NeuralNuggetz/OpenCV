import cv2 as cv
import os

webcam = cv.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    cv.imshow('Webcam Feed', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()