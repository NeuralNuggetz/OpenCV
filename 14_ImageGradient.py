import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def imageGradient():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//tesla1.jpg')
    img = cv.imread(imgPath)
    if img is None:
        print("Image not found.")
        return
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.subplot(221)
    plt.imshow(img, cmap='gray')

 # Calculate gradients using Sobel operator
    lap = cv.Laplacian(img, cv.CV_64F, ksize=21)
    plt.subplot(222)
    plt.imshow(lap, cmap='gray')

    # Sobel gradients in x and y directions
    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=21)
    plt.subplot(223)
    plt.imshow(sobelX, cmap='gray')

    sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=21)
    plt.subplot(224)
    plt.imshow(sobelY, cmap='gray')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    plt.show()

if __name__ == "__main__":
    imageGradient()