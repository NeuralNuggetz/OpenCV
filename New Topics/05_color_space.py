import cv2 as cv
import os

img = cv.imread(os.path.join('.', 'demoImages', 'tesla1.jpg'))

img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('Original Image', img)
cv.imshow('Image in RGB Color Space', img_RGB)
cv.waitKey(0)
cv.destroyAllWindows()