import cv2 as cv 
img = cv.imread("download.png")

if img is None:
    print("Oops! Image not found.")

else:
    print("Image Loaded Successfully.")
    pt1 = (300 , 50)
    pt2 = (450, 400)
    color = (0 , 0 , 255)
    thickness = 4

    cv.rectangle(img, pt1, pt2, color, thickness)

    cv.imshow("Rectangle Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()