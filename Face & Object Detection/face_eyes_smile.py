import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv.CascadeClassifier("haarcascade_smile.xml")

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1 , 10)
        if len(eyes) > 0:
            cv.putText(frame, "Eyes Detected", (x, y - 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7 , 20)
        if len(smiles) > 0:
            cv.putText(frame, "Smiling ", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 0), 2)


    cv.imshow("Smart Face Detection", frame)

    if  cv.waitKey(1) & 0xFF == ord("q"): 
        break

cap.release()
cv.destroyAllWindows()