import cv2 as cv
import os

img = cv.imread(os.path.join('.', 'demoImages', 'tesla1.jpg'))
print(f"Original image shape: {img.shape}")

# Crop the image
cropped_img = img[100:400, 100:400]
print(f"Cropped image shape: {cropped_img.shape}")

cv.imshow('Original Image', img)
cv.imshow('Cropped Image', cropped_img)
cv.waitKey(0)