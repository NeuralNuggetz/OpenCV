import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def harrisCornerDetection():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//tesla1.jpg')
    imgRGB = cv.cvtColor(cv.imread(imgPath), cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(imgRGB, cv.COLOR_RGB2GRAY)
    imgGray = np.float32(imgGray)

    
    plt.figure()
    plt.subplot(131)
    plt.imshow(imgGray, cmap='gray')

    plt.subplot(132)
    blockSize = 5
    sobelSize = 3
    k = 0.04
    harrisCorners = cv.cornerHarris(imgGray, blockSize, sobelSize, k)
    plt.imshow(harrisCorners)

    plt.subplot(133)
    imgRGB[harrisCorners > 0.01 * harrisCorners.max()] = [255, 0, 0]

    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    harrisCornerDetection()