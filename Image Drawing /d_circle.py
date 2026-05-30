import cv2 as cv 
img = cv.imread("download.png")

if img is None:
    print("Oops! Image not found.")

else:
    print("Image Loaded Successfully.")
    center = (400, 170)
    radius = 100
    color = (0, 0, 255)
    thickness = 4

    cv.circle(img, center, radius, color, thickness)

    cv.imshow("Circle Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()