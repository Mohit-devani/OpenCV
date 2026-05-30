import cv2 as cv

img = cv.imread("images.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

Contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, Contours, -1, (0, 255, 0), 3) 
cv.imshow("contours", img)
cv.waitKey(0)
cv.destroyAllWindows()