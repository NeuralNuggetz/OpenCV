import cv2 as cv
import os

img = cv.imread(os.path.join('.', 'demoImages', 'bear.jpg'))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.imshow('Original Image', img)
cv.imshow('Thresholded Image', thresh)
cv.waitKey(0)