import cv2 as cv
import os
import matplotlib.pyplot as plt


# Function to read and write a single pixel in an image
def readAndWriteSinglePixel():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    if img is None:
        print(f"Failed to load image at {img_path}")
        return
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(imgRGB)
    plt.show()

    eye_pixel = img[465, 1015]  # Accessing the pixel at (100, 100)
    imgRGB[465, 1015] = [255, 0, 0]  # Changing the pixel color to red

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    

def readAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    eye_region = img[1000:1200, 450:600]  # Accessing a region of pixels
    dy = 600- 450
    dx = 1200 - 1000

    startx = 900
    starty = 350

    imgRGB[ startx:startx + dx, starty:starty + dy] = eye_region #changing the region
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
if __name__ == "__main__":
    readAndWritePixelRegion()
    # Note: The function readAndWriteSinglePixel() currently only reads and displays the image.
    # You can modify it to write a single pixel or perform other operations as needed.