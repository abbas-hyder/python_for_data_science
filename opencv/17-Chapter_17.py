# Joining two images

import cv2 as cv
import numpy as np

# read mage
img = cv.imread("resources/mypic.jpeg")
img1 = cv.resize(img,(100,150))
#stacking same image

# 1- Horizontal stack
hor_img = np.hstack((img1,img1))

# 2-Vertical stack
ver_img = np.vstack((img1,img1))


cv.imshow("Horizontal",hor_img)
cv.imshow("Vertical",ver_img)
cv.waitKey(0)
cv.destroyAllWindows()

# You can only stack images with same shapes (width,height,color channel)
# we can not resize the stack image(function)
# Assignmemt you have to define a function to stack multiple images of different sizes & color tunes