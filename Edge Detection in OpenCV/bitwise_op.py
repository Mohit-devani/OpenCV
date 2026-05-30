import cv2 as cv 
import numpy as np

img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

cv.circle(img1, (150, 150), 100, 255, -1)
cv.rectangle(img2, (100, 100), (250, 250), 255, -1)

bitWise_and = cv.bitwise_and(img1, img2)
bitWise_or = cv.bitwise_or(img1, img2)
bitWise_xor = cv.bitwise_xor(img1, img2)
bitWise_not = cv.bitwise_not(img1)

cv.imshow("Image 1", img1)
cv.imshow("Image 2", img2)
cv.imshow("Bitwise AND", bitWise_and)
cv.imshow("Bitwise OR", bitWise_or)
cv.imshow("Bitwise XOR", bitWise_xor)
cv.imshow("Bitwise NOT", bitWise_not)
cv.waitKey(0)
cv.destroyAllWindows()