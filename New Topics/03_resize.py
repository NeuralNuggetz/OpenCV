import cv2 as cv
import os

img = cv.imread(os.path.join('.', 'demoImages', 'tesla1.jpg'))

resizeimg = cv.resize(img, (640, 480))
print(img.shape)
cv.imshow('Image', img)
cv.imshow('Resized Image', resizeimg)
cv.waitKey(0)