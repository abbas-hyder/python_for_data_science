#converting video to gray or black and white

## reading a video
import cv2 as cv
cap=cv.VideoCapture("resources/myvideo.mp4")

while(True):
    ret, frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #(thresh, binary) = cv.threshold(grayframe, 127,255,cv.THRESH_BINARY) # black and white display
      # to show in player 
    if ret ==True:
        cv.imshow("video",grayframe)
       #cv.imshow("black and white",binary) #for black and white display
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()