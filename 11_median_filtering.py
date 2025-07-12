import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def medianFiltering():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        exit()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # adding noise to the image
    noisyimg = imgRGB.copy()
    noiseProb = 0.05

    noise = np.random.rand(noisyimg.shape[0], noisyimg.shape[1])
    noisyimg[noise < noiseProb/2] = 0  # salt noise
    noisyimg[noise > 1 - noiseProb/2] = 255  # pepper noise

    imgFiltered = cv.medianBlur(noisyimg, 5)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(noisyimg)
    plt.subplot(1, 2, 2)
    plt.imshow(imgFiltered)
    plt.show()

if __name__ == "__main__":
    medianFiltering()