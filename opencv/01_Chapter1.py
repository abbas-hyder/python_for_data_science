## Reading and displaying an image
#import library
# add comment for checking git
import cv2 as cv
mypic = cv.imread("resources/mypic.jpeg")
cv.imshow("pehli image",mypic)
cv.waitKey(0)
