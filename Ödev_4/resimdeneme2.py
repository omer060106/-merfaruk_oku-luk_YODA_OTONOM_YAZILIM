import cv2
import numpy


resim1 = cv2.imread("renkpaleti.jpg")

resim2 = cv2.imread("renkpaleti.jpg",0) #resmin siyah beyaz hali



#cv2.imshow("resim deneme omer faruk okusluk",resim1)
#cv2.imshow("resim deneme omer faruk okusluk",resim2)

print("----------------------------------------------------------------------------------------------------------------------------------------")


print(resim1)

print(resim1.size)

print(resim1.dtype)

print(resim1.shape)


print("----------------------------------------------------------------------------------------------------------------------------------------")


print(resim2)

print(resim2.size)

print(resim2.dtype)

print(resim2.shape)


print("----------------------------------------------------------------------------------------------------------------------------------------")

print(resim1[(56,7)])

resim1[60,60] = [0,0,0]
resim1[60,61] = [0,0,0]
resim1[60,62] = [0,0,0]
resim1[60,63] = [0,0,0]
resim1[60,64] = [0,0,0]
resim1[60,65] = [0,0,0]
resim1[60,66] = [0,0,0]
resim1[60,67] = [255,255,255]

cv2.imshow("resim deneme omer faruk okusluk",resim1)

for i in range(612):
    resim1[60,i] = [0,0,0]

  
cv2.imshow("resim deneme omer faruk okusluk",resim1)



cv2.waitKey(0)

cv2.destroyAllWindows()
