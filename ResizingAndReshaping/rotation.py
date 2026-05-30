import cv2 as cv 

img = cv.imread("download.png") 

if img is None:
    print("Image not load")

else:
    (h ,w)  = img.shape[:2 ]

    center = (w//2, h//2)
    M = cv.getRotationMatrix2D(center, 90, 1) 
    rotated = cv.warpAffine(img, M, (w, h))

    cv.imshow("Rotated Image", rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()