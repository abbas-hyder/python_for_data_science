## WRITING IMAGE OR SAVING AN IMAGE

import cv2 as cv
img = cv.imread("resources/mypic.jpeg")
img1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(img1, 127,255,cv.THRESH_BINARY)

cv.imwrite("resources/gray_img.png",img1)
cv.imwrite("resources/black_white.png",binary)

