import numpy as np
import cv2 as cv
import os

# Function to read video from webcam and display it

def videoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

# Function to read video from file and display it

def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'demoVideos\\demo.mp4')
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('Video', frame)
        delay = int(1000 / cap.get(cv.CAP_PROP_FPS))
        if cv.waitKey(delay) & 0xFF == ord('q'):
            break

# Function to write video from webcam to file

def writeVideoToFile():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID') # Codec for AVI files
    root = os.getcwd()
    out_path = os.path.join(root, 'demoVideos\\output.avi')

    out = cv.VideoWriter(out_path, fourcc, 20.0, (640, 480)) # Adjust resolution as needed 20.0 is the FPS, (640, 480) is the frame size    

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv.imshow('Webcam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    # videoFromFile()
    writeVideoToFile()
