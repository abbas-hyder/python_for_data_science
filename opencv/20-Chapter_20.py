# spilit your videos into frames
import cv2 as cv
cap = cv.VideoCapture("resources/myvideo.mp4")

frameNumber=0
while(True):
    ret,frame =cap.read()
    if ret:
        cv.imwrite(f"resources/frames/frames_{frameNumber}.jpg",frame)
    else:
        break
    frameNumber = frameNumber+1
cap.realease()
