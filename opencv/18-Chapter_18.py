
# how to change the perspective of an image
import cv2 as cv
import numpy as np

img = cv.imread("resources/warp.jpg")
img = cv.resize(img, (500,800))
print(img.shape)

#defining points

point1 = np.float32([[102,106],[400,94],[20,549],[468,555]])  # firt argument for height and second for width
width = 500
height = 800


point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img,matrix,(width,height))

# stack both images
hor_img = np.hstack((img,out_img))
# cv.imshow("original",img)
# cv.imshow("transformed",out_img)
cv.imshow("transformed",hor_img)
cv.waitKey(0)
cv.destroyAllWindows()