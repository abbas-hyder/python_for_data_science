##GREY SCALE CONVERSION
import cv2 as cv
mypic = cv.imread("resources/mypic.jpeg")
mypic2 = cv.resize(mypic,(500,400))

grey_img = cv.cvtColor(mypic2,cv.COLOR_BGR2GRAY)

# display code
cv.imshow("grey",grey_img)
cv.imshow("resized image",mypic2)

#delay code
cv.waitKey(0)
cv.destroyAllWindows()