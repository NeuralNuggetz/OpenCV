import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(os.path.join('.', 'demoImages', 'basketball.jpg'))
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img_edges = cv.Canny(img, 100, 200)

img_dilate = cv.dilate(img_edges, np.ones((2, 2), np.uint8))

img_erode = cv.erode(img_dilate, np.ones((2, 2), np.uint8))

plt.figure()
plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(img_edges, cmap='gray')
plt.title('Edges')

plt.subplot(1, 4, 3)
plt.imshow(img_dilate, cmap='gray')
plt.title('Dilated Edges')

plt.subplot(1, 4, 4)
plt.imshow(img_erode, cmap='gray')
plt.title('Eroded Edges')

plt.show()