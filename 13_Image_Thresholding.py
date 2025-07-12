import cv2 as cv
import os 
import numpy as np
import matplotlib.pyplot as plt 

def threshold():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//tesla1.jpg')
    img = cv.imread(imgPath)
    if img is None:
        print("Image not found.")
        return
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([imgGray], [0], None, [256], [0, 256])
    plt.figure()
    plt.plot(hist)
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('number of Pixels')
    

    threshOpt = [cv.THRESH_BINARY,
                 cv.THRESH_BINARY_INV,
                 cv.THRESH_TRUNC,
                 cv.THRESH_TOZERO,
                 cv.THRESH_TOZERO_INV]
    
    threshNames = ['BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

    plt.figure()
    plt.subplot(231)
    plt.imshow(imgGray, cmap='gray')
    
    for i in range(len(threshOpt)):
        ret, thresh = cv.threshold(imgGray, 140, 255, threshOpt[i])
        plt.subplot(2, 3, i + 2)
        plt.imshow(thresh, cmap='gray')
        plt.title(threshNames[i])
        plt.axis('off')
    plt.show()
if __name__ == "__main__":
    threshold()