import cv2 as cv 
img = cv.imread("download.png")

if img is None:
    print("Oops! Image not found.")

else:
    print("Image Loaded Successfully.")
    pt1 = (200 , 50)
    pt2 = (300, 400)
    color = (0 , 0 , 255)
    thickness = 4

    cv.line (img , pt1, pt2 , color , thickness)

    cv.imshow("Line Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()