import cv2
import numpy as np


kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.rectangle(goruntu,(100,100),(200,200),(56,85,12),3)

    cv2.line(goruntu,(0,0),(100,100),(136,44,255),2)

    cv2.circle(goruntu,(150,150),50,(255,12,46),2)

    cv2.putText(goruntu,"omer",(250,250),cv2.FONT_HERSHEY_DUPLEX,1,(68,255,70),2)

    cv2.imshow("kendikamera denem",goruntu)

    if cv2.waitKey(25) & 0xFF==27:
        break






kamera.release()

cv2.destroyAllWindows()