import cv2 as cv
import os

img = cv.imread(os.path.join('.', 'demoImages', 'basketball.jpg'))

img_edge = cv.Canny(img, 150, 200)

cv.imshow('img', img)
cv.imshow('img_edge', img_edge)
cv.waitKey(0)