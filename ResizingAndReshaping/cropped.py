import cv2 as cv 

img = cv.imread("download.png")

if img is not None:
    cropped = img[0:700, 200:600]

    cv.imshow("Cropped Image", cropped)
    cv.imshow("Original Image", img)

    cv.waitKey(0)
    cv.destroyAllWindows()