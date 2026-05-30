import cv2

img = cv2.imread("Resources/images.jpeg")

cv2.imshow("My Image", img)
print(type(img))
print(img[0,0])
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()