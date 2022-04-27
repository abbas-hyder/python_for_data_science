# Resolution of cam
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#resolution HD(1280x720)

#creating function for hd resolution
def hd_resolution():
    cap.set(3,1280) # width
    cap.set(4,720)  # height

def sd_resolution():
    cap.set(3,640) # width
    cap.set(4,480)  # height

# Assignment how to change and fix the frame rate to 30fps
def fhd_resolution():
    cap.set(3,1920) # width
    cap.set(4,1000)  # height
    cap.set(cv.CAP_PROP_FPS,15)

fhd_resolution()

# hd_resolution()
# sd_resolution()


while(True):
    ret,frame = cap.read()
    if ret==True:
        cv.imshow("camera",frame)
        if cv.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()