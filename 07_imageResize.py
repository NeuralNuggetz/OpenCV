import cv2 as cv
import os
import matplotlib.pyplot as plt

def ImageSize():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    height, width, _ = imgRGB.shape

    plt.figure()
    plt.imshow(imgRGB)
    plt.title(f'Image Size: {width}x{height}')
    plt.show()

# Image Resizing
def imageResize():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\dog.png')
    img = cv.imread(imgPath)
    if img is None:
        print(f"Failed to load image at {imgPath}")
        return
    
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = img[420:493,1120:1197, :] # Cropping the image to a specific region
    height, width, _ = img.shape # Get the dimensions of the cropped image

    scale = 4 # Adjust the scale factor as needed 
    # 1/4 =  Sets the scaling factor to reduce the size by 4x (25% of original).
    # 1/2 =  Sets the scaling factor to reduce the size by 2x (50% of original).
    # 2 = Sets the scaling factor to increase the size by 2x (200% of original).
    # 4 = Sets the scaling factor to increase the size by 4x (400% of original).
    interpMethods = [
        cv.INTER_AREA,
        cv.INTER_NEAREST,
        cv.INTER_LINEAR,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]
    # Define the interpolation methods to be used for resizing
    # cv.INTER_AREA: Good for shrinking images.
    # cv.INTER_NEAREST: Fastest but may produce blocky results.
    # cv.INTER_LINEAR: Good for enlarging images, default for resizing.
    # cv.INTER_CUBIC: Better quality for enlarging images, slower than INTER_LINEAR.
    # cv.INTER_LANCZOS4: Best quality for enlarging images, uses a sinc function, slower than INTER_CUBIC.
    # cv.INTER_LINEAR_EXACT: Similar to INTER_LINEAR but uses exact linear interpolation.
    interpTitle = ['area', 'nearest', 'linear', 'cubic', 'lanczos4']

    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(img)



    # Perform resizing
    for i in range(len(interpMethods)):
        plt.subplot(2,3,i+2)
        imgResize = cv.resize(img, (int(width * scale), int(height * scale)), interpolation=interpMethods[i]) # Resize the image using the specified interpolation method
        # cv.resize() function is used to resize the image to a new size specified by (width * scale, height * scale).
        # The interpolation method is specified by interpMethods[i], which can be one of the methods defined earlier.
        # The new size is calculated by multiplying the original width and height by the scale factor.
        plt.imshow(imgResize)
        plt.title(interpTitle[i])
    plt.show()

if __name__ == "__main__":
    imageResize()
    # Note: The function imageResize() currently only reads and displays the resized images.
    # You can modify it to perform other operations as needed.
    # ImageSize()