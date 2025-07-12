import cv2 as cv
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # This import is needed for 3D plotting
import numpy as np

def callbacks(x):
    pass

def gaussianKernel(size, sigma):
    kernel = cv.getGaussianKernel(size, sigma)
    kernel = kernel * kernel.T  # Create a 2D Gaussian kernel
    return kernel

def gaussianFiltering():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages//dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        exit()
    n = 51
    fig = plt.figure()
    plt.subplot(121) 
    kernel = gaussianKernel(n, 8)
    plt.imshow(kernel)
    ax = fig.add_subplot(122, projection='3d')  # Create a 3D subplot
    x = np.linspace(0, n - 1, n)
    y = np.linspace(0, n - 1, n)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, kernel, cmap='viridis')  # Use the 3D axes object
    plt.show()

    winName = 'Gaussian Filter'
    cv.namedWindow(winName)
    cv.createTrackbar('sigma', winName, 1, 100, callbacks)
    height, width, _ = img.shape
    scale = 1 / 4
    width = int(width * scale)
    height = int(height * scale)
    img = cv.resize(img, (width, height))

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        sigma = cv.getTrackbarPos('sigma', winName)
        imgFilter = cv.GaussianBlur(img, (n, n), sigma)
        cv.imshow(winName, imgFilter)
    cv.destroyAllWindows()

if __name__ == "__main__":
    gaussianFiltering()   