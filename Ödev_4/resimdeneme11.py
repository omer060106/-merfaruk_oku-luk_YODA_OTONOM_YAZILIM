import cv2
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(153,24,170),3)

cv2.circle(resim,(150,150),25,(123,90,12),4)


cv2.putText(resim,"OMER FARUK",(10,200),cv2.FONT_HERSHEY_COMPLEX,1,(90,160,70),2)

cv2.imshow("deneme line",resim)


cv2.waitKey(0)
cv2.destroyAllWindows() 

