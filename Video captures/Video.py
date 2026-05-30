import cv2 as cv 

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret=True/False , frame = img

    if not ret:
        print("Failed to grab frame")
        break

    cv.imshow("Webcam feed", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

cap.release()
cv.destroyAllWindows()