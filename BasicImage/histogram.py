# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("Resources/download.png")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# plt.plot(hist)
# plt.title("Grayscale Histogram")
# plt.show()
#---------------------------------------------
# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("Resources/download.png")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# plt.plot(hist)
# plt.title("Grayscale Histogram")
# plt.show()

#----------------------

import cv2

img = cv2.imread("Resources/download.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()