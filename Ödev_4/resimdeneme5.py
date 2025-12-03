import cv2
import numpy


resim = cv2.imread("hababam.jpg")

cv2.rectangle(resim,(240,220),(305,125),[0,0,255],3)


cv2.imshow("resim deneme omer faruk okusluk",resim)




cv2.waitKey(0)
cv2.destroyAllWindows()
