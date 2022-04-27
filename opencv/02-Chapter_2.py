## Resizing the image

#import library
import cv2 as cv
from cv2 import imshow
mypic = cv.imread("resources/mypic.jpeg")
mypic2 = cv.resize(mypic,(500,400))

# display
cv.imshow("original",mypic)
cv.imshow("resized image",mypic2)
cv.waitKey(0)
cv.destroyAllWindows()
