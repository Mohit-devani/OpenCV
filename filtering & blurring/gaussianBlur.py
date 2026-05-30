import cv2 as cv 
img = cv.imread("people.jpg") 

blurred = cv.GaussianBlur(img, (17, 17), 0)
cv.imshow ("Original Image", img)
cv.imshow ("Blurred Image", blurred)

cv.waitKey(0)
cv.destroyAllWindows()