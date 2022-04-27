## reading a video
import cv2 as cv
cap=cv.VideoCapture("resources/myvideo.mp4")

#indicati=or to show video is working
if(cap.isOpened()==False):
    print("Error in video")
#reading and playing
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break
cap.release()
cv.destroyAllWindows()
