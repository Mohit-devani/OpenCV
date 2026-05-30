import cv2 as cv 

img = cv.imread("download.png") 

if img is None:
    print("Image not load")

else:
   
    flipped_vertical = cv.flip(img, 0)
    flipped_horizontal = cv.flip (img, 1)
    flipped_both = cv.flip (img, -1)

    cv.imshow("Original Image", img)
    cv.imshow("Flipped Horizontal", flipped_horizontal) 
    cv.imshow("Flipped Vertical", flipped_vertical)
    cv.imshow("Flipped Both", flipped_both)
    cv.waitKey(0)
    cv.destroyAllWindows()