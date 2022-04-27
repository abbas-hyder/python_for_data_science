# Basic functions or Manipulation in opencv
import cv2 as cv
import numpy as np
img = cv.imread("resources/mypic.jpeg")
print("the size of my image = ",img.shape)

# resize function
resized_img = cv.resize(img,(150,250))

# Gray_Image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Black & White image
(thresh, binary) = cv.threshold(gray_img, 127,255,cv.THRESH_BINARY)
# Blurred Image
blur_img = cv.GaussianBlur(img,(7,7), 0) # (7,7) is image intensity always odd you can increase or decrease blur by changing values

# Edge detection
edge_img = cv.Canny(img, 48,48) # 48,48 threshould1 and threshould 2

# thikness of lines
mat_kernal = np.ones((3,3),np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernal),iterations=1) #dilated means change the thikm=ness of edges

# make thiner outline
ero_img = cv.erode(dilated_img,(mat_kernal),iterations=1)

# for croping image we will use numpy not opencv
croped_img = img[0:500,0:350] #0:500 height & 0:350 width



cv.imshow("original",img)
# cv.imshow("Resized",resized_img)
# cv.imshow("Gray Image",gray_img)
# cv.imshow("B&G",binary)
# cv.imshow("Blured Img",blur_img) 
# cv.imshow("Edge",edge_img)
# cv.imshow("dilated img",dilated_img)
# cv.imshow("Erosion",ero_img)
cv.imshow("Crop Image",croped_img)
cv.waitKey(0)
cv.destroyAllWindows()

 