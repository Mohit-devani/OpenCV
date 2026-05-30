import cv2 as cv 
img = cv.imread("images.jpeg" , cv.IMREAD_GRAYSCALE)

edges = cv.Canny(img , 50 , 100)

cv.imshow("Original Image" , img)
cv.imshow("Edges" , edges)
cv.waitKey(0)
cv.destroyAllWindows()