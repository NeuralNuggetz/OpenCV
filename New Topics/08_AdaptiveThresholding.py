import cv2 as cv
import os
import matplotlib.pyplot as plt

img = cv.imread(os.path.join('.', 'demoImages', 'bear.jpg'))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Adaptive Thresholding
thresh1 = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cv.waitKey(0)