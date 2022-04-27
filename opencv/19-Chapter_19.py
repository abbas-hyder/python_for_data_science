# coordinates of an image or video
# bgr color codes from an image

# step-1 Import librraries
import cv2 as cv
import numpy as np

# step-2 define function
def find_coord(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
       #left mouse click
        print(x, '',y)
      #how to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) + ','+ str(y),(x,y),font,1,(255,0,0),thickness=2)
      #show the text on image and image itself
        cv.imshow("image",img)
    #for color finding
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        font = cv.FONT_HERSHEY_PLAIN
        b= img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]

        cv.putText(img, str(b)+',' + str(g) +',' + str(r),(x,y),font,1,(255,0,255),thickness=1)
        cv.imshow("image",img)

# step-3 final function to read and display
if __name__=="__main__":
    #reading an image
    img = cv.imread("resources/warp.jpg",1)
    #resize image
    img = cv.resize(img,(500,800))
    #display the image
    cv.imshow("image",img)
    #seting call back function
    cv.setMouseCallback("image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()