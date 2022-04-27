# how to draw lines and shapes in python

import cv2 as cv
import numpy as np


#draw a canvs 0 is for black 
img  = np.zeros((600,600))
img1 = np.ones((600,600))

#print size
print("The size of our canvas is  =",img.shape)


#adding colors to the canvas

colored_img = np.zeros((600,600,3),np.uint8) #color channel addition
colored_img[:] = 255,0,255 #color complete image
colored_img[150:230,100:207]=255,0,0 #color part of image

#adding line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)

cv.line(colored_img,(100,100),(600,600),(255,0,240),3 )
#adding rectangle
cv.rectangle(colored_img,(50,100),(300,400),(205,240,0),3) #Draw rectangle
cv.rectangle(colored_img,(50,100),(300,400),(205,240,0),cv.FILLED) #Fill Rectangle

#Adding circle
cv.circle(colored_img,(300,300),50,(255,100,0),5)
cv.circle(colored_img,(300,300),50,(255,100,0),cv.FILLED)

# adding text
cv.putText(colored_img,"python opencv",(200,50),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),2)
#assignment how to break above text into two lines 





# cv.imshow("black canvas",img)
# cv.imshow("white camvas",img1)
cv.imshow("colored ",colored_img)
cv.waitKey(0)
cv.destroyAllWindows()