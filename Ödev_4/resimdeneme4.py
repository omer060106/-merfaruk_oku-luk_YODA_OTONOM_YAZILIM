import cv2
import numpy

resim = cv2.imread("insanresim.jpg")

aynalama=cv2.copyMakeBorder(resim,300,300,250,250,cv2.BORDER_REFLECT)

uzatılan=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_REPLICATE)

tekrar=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_WRAP)
cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                           value=(75,150,150))


cv2.imshow("insan resim deneme omer faruk okusluk",cerceve)

cv2.waitKey(0)
cv2.destroyAllWindows()
