import cv2
import numpy

resim = cv2.imread("renkpaleti.jpg",0)

ret,thresh1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(resim,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(resim,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("orijinal",resim)
cv2.imshow("thresh deneme",thresh1)
cv2.imshow("thresh denemee",thresh2)
cv2.imshow("thresh denemeee",thresh3)
cv2.imshow("thresh denemeeee",thresh4)
cv2.imshow("thresh denemeeee",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
