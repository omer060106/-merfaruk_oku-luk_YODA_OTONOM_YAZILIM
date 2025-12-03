import cv2
import numpy as np


kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.imshow("kendikamera denem",goruntu)

    if cv2.waitKey(30) & 0xFF ==('x'):
        break

kamera.release()

cv2.destroyAllWindows()