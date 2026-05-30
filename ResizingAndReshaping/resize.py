import cv2 as cv 

img = cv.imread("download.png")

if img is None:
    print("Image not found ")

else:
    print("Image loaded")

    resized = cv.resize(img, (300, 300))

    cv.imshow("Resized Image", resized)
    cv.imshow("Original Image", img)

    cv.imwrite("ResizingAndReshaping/resized.png", resized)

    cv.waitKey(0)
    cv.destroyAllWindows()
