## Reading and displaying an image
#import library
import cv2 as cv
mypic = cv.imread("resources/mypic.jpeg")
cv.imshow("pehli image",mypic)
cv.waitKey(0)