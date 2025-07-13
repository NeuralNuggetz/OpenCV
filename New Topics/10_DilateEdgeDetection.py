import cv2 as cv
import os
import numpy as np

img = cv.imread(os.path.join('.', 'demoImages', 'basketball.jpg'))

img_edges = cv.Canny(img, 100, 200)

img_dilate = cv.dilate(img_edges, np.ones((2, 2), np.uint8))

cv.imshow('Original Image', img)
cv.imshow('Edges', img_edges)
cv.imshow('Dilated Edges', img_dilate)
cv.waitKey(0)