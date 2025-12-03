import cv2
import numpy

resim = cv2.imread("resimtoplama1.jpg")

resim1 = cv2.imread("resimtoplama2.jpg")



cv2.imshow("deneme omer faruk okusluk",resim)
cv2.imshow("deneme2 omer fxaruk okusluk",resim1)

resim1 = cv2.resize(resim1, (resim.shape[1], resim.shape[0]))


toplam=cv2.add(resim1,resim)

agirliklitop=cv2.addWeighted(resim,0.7,resim1,0.3,0)

cv2.imshow("toplanmıs resim",toplam)

cv2.imshow("toplanmııs resim",agirliklitop)

cv2.waitKey(0)
cv2.destroyAllWindows()
