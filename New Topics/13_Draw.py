import cv2 as cv
import os


img = cv.imread(os.path.join('.', 'demoImages', 'board.jpg'))
print(img.shape)

# Line drawing
cv.line(img, (180, 150), (300, 200), (455, 0, 0), 5)


# Rectangle drawing
cv.rectangle(img, (200, 350), (450, 600), (0, 255, 0), 3) # if the thickness is -1 replace of 3, it will fill the rectangle

# Circle drawing
cv.circle(img, (400, 100), 50, (0, 0, 255), -1) # -1 means filled circle

# text drawing

cv.putText(img, 'OpenCV Drawing', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.imshow('Drawn Shapes', img)
cv.waitKey(0)