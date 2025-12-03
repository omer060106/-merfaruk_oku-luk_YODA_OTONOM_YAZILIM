import cv2
import numpy as np

resim = cv2.imread("siyahbeyaz.jpg")

gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

bulanık = cv2.GaussianBlur(gri, (5, 5), 0)

_, esik = cv2.threshold(bulanık, 120, 255, cv2.THRESH_BINARY)

konturlar, _ = cv2.findContours(esik, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in konturlar:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(resim, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Orjinal", resim)
cv2.imshow("Esiklenmis", esik)
cv2.waitKey(0)
cv2.destroyAllWindows()
