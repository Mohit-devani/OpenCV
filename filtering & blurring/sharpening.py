import cv2 as cv 
import numpy as np

img = cv.imread("people.jpg") 

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv.filter2D(img, -1, sharpen_kernel) 
cv.imshow ("Original Image", img)
cv.imshow ("Sharpened Image", sharpened)
cv.waitKey(0)
cv.destroyAllWindows()