import cv2 as cv
import os
import numpy as np

videoPath = os.path.join('.', 'demoVideos', 'demo.mp4')

video = cv.VideoCapture(videoPath)

while True:
    ret, frame = video.read()
    if ret:
        cv.imshow('Video Frame', frame)
        cv.waitKey(30)
            

video.release()
cv.destroyAllWindows()