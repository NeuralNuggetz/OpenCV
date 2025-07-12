import cv2 as cv
import os

# Function to convert an image to grayscale and display it
def graysScale():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path)
    if img is None:
        print(f"Failed to load image at {img_path}")
        return
    
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayscale Image', imgGray)
    cv.waitKey(0)

# Function to read an image as grayscale and display it
# This function is similar to graysScale but uses cv.IMREAD_GRAYSCALE
# It is useful for directly reading an image in grayscale mode without converting it later.
# save one line of code
def readAsGray():
    root = os.getcwd()
    img_path = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Failed to load image at {img_path}")
        return
    
    cv.imshow('Grayscale Image', img)
    cv.waitKey(0)

if __name__ == "__main__":
    # graysScale()
    # Note: The function graysScale() currently only reads and displays the grayscale image.
    # You can modify it to perform other operations as needed.
    readAsGray()