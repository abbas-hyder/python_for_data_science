#converting video to gray or black and white And Saving 

## reading a video
import cv2 as cv
from matplotlib.colors import is_color_like

cap=cv.VideoCapture("resources/myvideo.mp4")

#writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/OutVideo.avi",cv.VideoWriter_fourcc('M',"j",'P','G'),10,(frame_width,frame_height),isColor=False)
while(True):
    ret, frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
      # to show in player 
    if ret ==True:
        out.write(grayframe)
        cv.imshow("video",grayframe)
        #cv.imshow("black and white",binary) #for black and white display
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()