import cv2
import numpy 

resim = cv2.imread("hababam.jpg")

ikikatB=cv2.pyrUp(resim)

ikikatK=cv2.pyrDown(resim)


print("orijinal resim",resim.shape)
print("ikikat buyuk resim",ikikatB.shape)
print("ikikat kucuk resim",ikikatK.shape)

cv2.imshow("orijinal", resim)
cv2.imshow("ikikat buyultulmus",ikikatB)
cv2.imshow("ikikat kucultulmus",ikikatK)



cv2.waitKey(0)
cv2.destroyAllWindows()