import cv2 as cv
import os
import matplotlib.pyplot as plt

img = cv.imread(os.path.join('.', 'demoImages', 'bear.jpg'))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh1 = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)

thresh = cv.blur(thresh1, (20, 20))
ret, thresh2 = cv.threshold(thresh, 90, 255, cv.THRESH_BINARY)

plt.figure(figsize=(12, 4))

# Show original image
plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Show thresholded image
plt.subplot(1, 3, 2)
plt.imshow(thresh1, cmap='gray')
plt.title('Thresholded Image')
plt.axis('off')

# Show blurred + thresholded image
plt.subplot(1, 3, 3)
plt.imshow(thresh2, cmap='gray')
plt.title('Blurred Thresholded Image')
plt.axis('off')

plt.tight_layout()
plt.show()
