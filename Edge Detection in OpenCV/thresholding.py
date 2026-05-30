import cv2 as cv 
img = cv.imread("images.jpeg" , cv.IMREAD_GRAYSCALE)

ret , thresh = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)

cv.imshow("Original Image" , img)
cv.imshow("Thresholded Image" , thresh)
cv.waitKey(0)
cv.destroyAllWindows() 