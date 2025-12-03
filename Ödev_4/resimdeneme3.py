import cv2
import numpy

resim = cv2.imread("insanresim.jpg")

cv2.imshow("insan resim deneme omer faruk okusluk",resim)


#resim[:,:,0]=100
#resim[:,:,1]=10

resim[60:380,280:650,0]=255


cv2.imshow("insan resim deneme omer faruk okusluk",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
