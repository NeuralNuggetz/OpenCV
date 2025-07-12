import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def cannyEdge():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//tesla1.jpg')
    img = cv.imread(imgPath)
    if img is None:
        print("Image not found.")
        return
    img = cv.imread(imgPath, cv.COLOR_BGR2RGB)


    height, width, _ = img.shape
    scale = 1/5
    heightScaled = int(height * scale)
    widthScaled = int(width * scale)

    # Resize the image to reduce processing time
    img = cv.resize(img, (widthScaled, heightScaled), interpolation=cv.INTER_AREA)

    winname = 'Canny Edge Detection'
    cv.namedWindow(winname)
    cv.createTrackbar('minThres',winname, 0, 255, lambda x: None)
    cv.createTrackbar('maxThres',winname, 0, 255, lambda x: None)

    while True:
        if cv.waitKey(1) == ord('q'):
            break
        minThres = cv.getTrackbarPos('minThres', winname)
        maxThres = cv.getTrackbarPos('maxThres', winname)
        cannyEdge = cv.Canny(img, minThres, maxThres)
        cv.imshow(winname, cannyEdge)

    cv.destroyAllWindows()

if __name__ == "__main__":
    cannyEdge()
