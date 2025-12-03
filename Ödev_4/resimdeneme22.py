import cv2
import numpy as np

resim = cv2.imread("kup.jpg")

h, w = resim.shape[:2]

 
pts1 = np.float32([[0,0], [w-1,0], [0,h-1]])
pts2 = np.float32([[20,30], [w-50,10], [30,h-20]])

M_affine = cv2.getAffineTransform(pts1, pts2)
affine_sonuc = cv2.warpAffine(resim, M_affine, (w, h))

 
pts1_p = np.float32([[0,0], [w,0], [0,h], [w,h]])
pts2_p = np.float32([[30,30], [w-30,10], [20,h-20], [w-40,h-40]])

M_pers = cv2.getPerspectiveTransform(pts1_p, pts2_p)
pers_sonuc = cv2.warpPerspective(resim, M_pers, (w, h))

cv2.imshow("Orjinal", resim)
cv2.imshow("Affine Dönüsüm", affine_sonuc)
cv2.imshow("Perspektif Dönüsüm", pers_sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()
