import cv2 as cv
import os
import matplotlib.pyplot as plt

root = os.getcwd()
imgPath = os.path.join(root, 'demoImages\\freelancer.jpeg')
img = cv.imread(imgPath)
if img is None:
    print(f"Failed to load image at {imgPath}")
    exit()
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.figure(figsize=(8,8))
plt.imshow(img)
plt.title('Click top-left and bottom-right corners to crop')
pts = plt.ginput(2)
plt.close()

x1, y1 = map(int, pts[0])
x2, y2 = map(int, pts[1])
print(f"Cropping from: ({x1}, {y1}) to ({x2}, {y2})")

cropped_img = img[y1:y2, x1:x2, :]
print(f"Cropped image shape: {cropped_img.shape}")

plt.imshow(cropped_img)
plt.title('Cropped Image')
plt.show()
