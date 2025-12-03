import cv2
import numpy

resim = cv2.imread("parmakizi.jpg",0)


ret,thresh1=cv2.threshold(resim,160,255,cv2.THRESH_BINARY)

thresh2=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                              cv2.THRESH_BINARY,25,8)

thresh3=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,11,2)
cv2.imshow("orijinal",resim)
cv2.imshow("thresh deneme",thresh1)
cv2.imshow("thresh denemee",thresh2)
cv2.imshow("thresh denemeee",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()
