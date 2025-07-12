import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def grayHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)  # Load image in grayscale
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    plt.figure()
    plt.imshow(img, cmap='gray')

    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel('number of pixels')
    plt.show()

def colorHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    colors = ['red', 'green', 'blue']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=colors[i])
        plt.xlim([0, 256])
    plt.xlabel('bins')
    plt.ylabel('number of pixels')
    plt.title('Color Histogram')
    plt.show()

def histogramRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgRGB = imgRGB[255:1227, 906:2100, :]  # Crop the image to a region of interest
    plt.figure()
    plt.imshow(imgRGB)

    colors = ['red', 'green', 'blue']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB], [i], None, [256], [0, 256])
        plt.plot(hist, color=colors[i])

    plt.xlabel('bins')
    plt.ylabel('number of pixels')
    plt.title('Color Histogram for Region of Interest')
    plt.show()

if __name__ == "__main__":
    # grayHistogram()
    # colorHistogram()
    histogramRegion()
    # Note: The function grayHistogram() currently only reads and displays the histogram.
    # You can modify it to perform other operations as needed.