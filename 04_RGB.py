import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


# Function to create and display pure color images for each channel
def pureColor():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros, zeros, 255*ones))  # Blue channel
    gImg = cv.merge((zeros, 255*ones, zeros))  # Green channel
    rImg = cv.merge((255*ones, zeros, zeros))  # Red channel
    blackImg = cv.merge((zeros, zeros, zeros))  # Black channel
    whiteImg = cv.merge((255*ones, 255*ones, 255*ones))  # White channel

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('Blue Channel')
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('Green Channel')
    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('Red Channel')
    plt.subplot(234)
    plt.imshow(blackImg)
    plt.title('Black Channel')
    plt.subplot(235)
    plt.imshow(whiteImg)
    plt.title('White Channel')
    plt.show()

# Function to convert BGR image to grayscale and display
def bgrChannelGrayScale():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    if img is None:
        print(f"Failed to load image at {img_path}")
        return
    '''
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    b_channel, g_channel, r_channel = cv.split(imgRGB)

    plt.figure()
    plt.subplot(131)
    plt.imshow(b_channel, cmap='gray')
    plt.title('Blue Channel')
    plt.subplot(132)
    plt.imshow(g_channel, cmap='gray')
    plt.title('Green Channel')
    plt.subplot(133)
    plt.imshow(r_channel, cmap='gray')
    plt.title('Red Channel')
    plt.show()
    '''

    # or code to split the channels and display them separately
    # Uncomment the following lines if you want to visualize the channels separately

    r,g,b = cv.split(img)  # Split the image into 

    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap='gray')
    plt.title('Blue Channel')
    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('Green Channel')
    plt.subplot(133)
    plt.imshow(r, cmap='gray')
    plt.title('Red Channel')
    plt.show()

# Function to convert BGR image to grayscale and display
def bgrChannelColor():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    if img is None:
        print(f"Failed to load image at {img_path}")
        return
    r,g,b = cv.split(img)  # Split the image into BGR channels
    zeros = np.zeros_like(r)
    r_channel = cv.merge((r, zeros, zeros))  # Red channel
    g_channel = cv.merge((zeros, g, zeros))  # Green channel
    b_channel = cv.merge((zeros, zeros, b))  # Blue channel

    plt.figure()
    plt.subplot(131)
    plt.imshow(b_channel)
    plt.title('Blue Channel')
    plt.subplot(132)
    plt.imshow(g_channel)
    plt.title('Green Channel')
    plt.subplot(133)
    plt.imshow(r_channel)
    plt.title('Red Channel')
    plt.show()

if __name__ == "__main__":
    # pureColor()
    # Note: The function pureColor() creates and displays pure color images for each channel.
    # You can modify it to perform other operations as needed.
    # bgrChannelGrayScale()
    bgrChannelColor()