import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def convolution2d():
    root = os.getcwd()
    imgpath = os.path.join(root, 'demoImages//dog.png')
    img = cv.imread(imgpath)
    if img is None:
        print(f"Failed to load image at {imgpath}")
        exit()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    n = 100
    kernel = np.ones((n, n), np.float32) / (n * n)
    imgFiltered = cv.filter2D(imgRGB, -1, kernel)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(imgRGB)
    plt.subplot(1, 2, 2)
    plt.imshow(imgFiltered)
    plt.show()

if __name__ == "__main__":
    convolution2d()