import cv2
import numpy

resim = cv2.imread("logoyildiz.png")

resim = cv2.imread("logoyildiz.png",0)



cv2.imshow("logo deneme omer faruk okusluk",resim)

cv2.imwrite("yeniresim.png",resim)


cv2.waitKey(0)

cv2.destroyAllWindows()
