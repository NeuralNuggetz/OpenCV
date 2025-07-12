import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def readImage():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    debug = 1
    if img is not None:
        cv.imshow('img', img)
    else:
        print(f"Failed to load image at {img_path}")
    cv.waitKey(0)

def writeImage():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    if img is not None:
        cv.imwrite('demoImages\\dog_copy.png', img)
    else:
        print(f"Failed to load image at {img_path}")

if __name__ == "__main__":
    readImage()
    writeImage()
