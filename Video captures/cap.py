import cv2 as cv 

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret = true/ false , frame = image

    if not ret:
        print ("cound not read frame ")
        break

    cv.imshow("Webcam feed", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Quitting.....")
        break
cap.release()
cv.destroyAllWindows()
 