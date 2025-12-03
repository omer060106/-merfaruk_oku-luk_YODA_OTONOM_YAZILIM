import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    if not ret:
        break

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Orjinal", frame)
    cv2.imshow("Gri", gri)

    if cv2.waitKey(1) & 0xFF == 27:
        break

kamera.release()
cv2.destroyAllWindows()
