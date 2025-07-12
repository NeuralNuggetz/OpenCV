import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def average_filtering():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        exit()
    winName = 'avg filter'
    cv.namedWindow(winName)
    cv.createTrackbar('n', winName, 1, 100, lambda x: None)

    height, width, _ = img.shape
    scale = 1/4
    width = int(width * scale)
    height = int(height * scale)
    img = cv.resize(img, (width, height))

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        n = cv.getTrackbarPos('n', winName)
        imgFilter = cv.blur(img, (n, n))
        cv.imshow(winName, imgFilter)
    cv.destroyAllWindows()

if __name__ == "__main__":
    average_filtering()

