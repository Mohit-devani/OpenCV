import cv2 as cv 
img = cv.imread("download.png")

if img is None:
    print("Oops! Image not found.")

else:
    print("Image Loaded Successfully.")
    text = "OpenCV is too much fun!"
    org = (50, 50)
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0 , 0 ,255)
    thickness = 4

    cv.putText(img, text, org, font, fontScale, color, thickness)

    cv.imshow("Adding text over image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()