import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvColorSegmentation():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerBound = np.array([0, 0, 50])
    upperBound = np.array([10, 220, 255])
    mask = cv.inRange(hsv, lowerBound, upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow('mask', mask)
    cv.waitKey(0)

if __name__ == "__main__":
    hsvColorSegmentation()
    # Note: The function hsvColorSegmentation() currently only reads and displays the mask.
    # You can modify it to perform other operations as needed.