import cv2
import numpy 

resim = cv2.imread("hababam.jpg")

resimgri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)


yükseklik,genislik,kanalsaiyisi =resim.shape
print("sayılar",yükseklik,genislik,kanalsaiyisi)

yüksek,genis=resimgri.shape
print("sayilar",yüksek,genis)


cv2.imshow("orijinal", resim)
cv2.imshow("grilestirilmis resim", resimgri)

cv2.waitKey(0)
cv2.destroyAllWindows()