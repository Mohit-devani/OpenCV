import cv2 as cv

img = cv.imread("shapessss.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

Contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, Contours, -1, (0, 255, 0), 3) 

for contour in Contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    elif corners == 6:
        shape_name = "Hexagon"

    elif corners == 11:
        shape_name = "Star"

    else:
        shape_name = "Circle"

    cv.drawContours(img, [approx], 0, (0, 255, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    cv.putText(img, shape_name, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2) 



cv.imshow("contours", img)
cv.waitKey(0)
cv.destroyAllWindows()