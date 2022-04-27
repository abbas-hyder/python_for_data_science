## CONVERT AN IMAGE INTO BLACK AND WHITE IMAGE

import cv2 as cv
from cv2 import threshold
from cv2 import imshow
img = cv.imread("resources/mypic.jpeg")
img1 = cv.resize(img,(500,400))

gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127,255,cv.THRESH_BINARY)

cv.imshow("original",img1)
cv.imshow("gray",gray)
cv.imshow("Black and white",binary)

cv.waitKey(0)
cv.destroyAllWindows()
