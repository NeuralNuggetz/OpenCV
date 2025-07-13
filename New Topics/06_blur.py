import cv2 as cv
import os
import matplotlib.pyplot as plt

img = cv.imread(os.path.join('.', 'demoImages', 'freelancer.jpeg'))

k = 7

img_blur = cv.blur(img, (k, k))
cv.imshow('Original Image', img)
cv.imshow('Blurred Image', img_blur)

# Define face region coordinates
y1, y2 = 92, 189
x1, x2 = 381, 487

# Apply blur on the region of interest (ROI) without cropping the original image
roi = img[y1:y2, x1:x2]
roi_blur = cv.blur(roi, (k, k))

# Place the blurred ROI back into the original image
img_blurred_face = img.copy()
img_blurred_face[y1:y2, x1:x2] = roi_blur
cv.imshow('Blurred Face in Full Image', img_blurred_face)



# Gaussian blur
img_gaussian_blur = cv.GaussianBlur(img, (k, k), 0)
cv.imshow('Gaussian Blurred Image', img_gaussian_blur)

# Median blur
img_median_blur = cv.medianBlur(img, k)
cv.imshow('Median Blurred Image', img_median_blur)

cv.waitKey(0)
cv.destroyAllWindows()