import cv2
import numpy as np

resim=cv2.imread("kirligoruntu1.png")

filtre=cv2.blur(resim,(3,3))
filtre2=cv2.blur(resim,(5,5))
filtre3=cv2.blur(resim,(10,10))

filtre4=cv2.medianBlur(resim,3)
filtre5=cv2.medianBlur(resim,5)

filtre6=cv2.GaussianBlur(resim,(3,3),0)
filtre7=cv2.GaussianBlur(resim,(5,5),0)
filtre8=cv2.GaussianBlur(resim,(7,7),0)




cv2.imshow("kirli gorunteu",resim)
#cv2.imshow("az kirli gorunteu",filtre)
#cv2.imshow("daha az kirli gorunteu",filtre2)
cv2.imshow("daha az kirli gorunteu",filtre3)
cv2.imshow(" daha daha az kirli gorunteu",filtre4)
cv2.imshow(" çok daha az kirli gorunteu",filtre5)
cv2.imshow("Gauss daha az kirli gorunteu",filtre6)
cv2.imshow(" Gaussdaha daha az kirli gorunteu",filtre7)
cv2.imshow(" Gaussçok daha az kirli gorunteu",filtre8)


cv2.waitKey(0)
cv2.destroyAllWindows()

