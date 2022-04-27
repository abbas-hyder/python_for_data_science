# Setting of camera or video
 
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

cap.set(10,100) # 10 is the key to set t6he brightness
cap.set(3,300)  # 3 is key of width
cap.set(4,100)  # 4 is key of height
while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()