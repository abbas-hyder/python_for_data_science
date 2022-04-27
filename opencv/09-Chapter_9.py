# How to connect web cam to python
#step 1 import libraries
import cv2 as cv
import numpy as np

#step 2 Read the frames from camera
cap = cv.VideoCapture(0) # zero means web cam number one

# read cam until the end
# step 3: dsiplay frame by frame

while(cap.isOpened()):
    #read frame by frame
    ret, frame = cap.read()
    if ret == True:
        #to display frames
        cv.imshow("mycam",frame)
        #to quit the loop with q
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
      break
cap.release()
cv.destroyAllWindows()