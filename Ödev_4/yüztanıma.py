import cv2
import time


face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

merkezler = []

sure_baslangic = None
yuz_var = False

while True:
    ok, kare = cam.read()
    if not ok:
        break

    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

    yuzler = face.detectMultiScale(gri, 1.3, 5)

    if len(yuzler) > 0:

        x, y, w, h = yuzler[0]

        cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 2)


        cx = x + w // 2
        cy = y + h // 2

        cv2.putText(kare, f"({cx},{cy})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        merkezler.append((cx, cy))

        if len(merkezler) > 60:
            merkezler.pop(0)


        for i in range(1, len(merkezler)):
            cv2.line(kare, merkezler[i-1], merkezler[i], (0, 0, 255), 2)

        if not yuz_var:
            yuz_var = True
            sure_baslangic = time.time()

        gecen = int(time.time() - sure_baslangic)
        cv2.putText(kare, f"{gecen} s", (kare.shape[1]-100, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    else:

        yuz_var = False
        sure_baslangic = None
        merkezler.clear()


    cv2.imshow("Kamera", kare)

    if cv2.waitKey(1) == 27: #esc tuşunun asscII tablosu karşılığı
        break

cam.release()
cv2.destroyAllWindows()
