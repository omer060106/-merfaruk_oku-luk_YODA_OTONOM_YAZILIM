import cv2
import numpy as np


resim = cv2.imread("uzay.jpg")


kernel = np.ones((5,5), np.uint8)

daraltma = cv2.erode(resim, kernel, iterations=1)


genisleme = cv2.dilate(daraltma, kernel, iterations=1)


opening = cv2.morphologyEx(resim, cv2.MORPH_OPEN, kernel)


closing = cv2.morphologyEx(resim, cv2.MORPH_CLOSE, kernel)


gradyan = cv2.morphologyEx(resim, cv2.MORPH_GRADIENT, kernel)


tophat = cv2.morphologyEx(resim, cv2.MORPH_TOPHAT, kernel)


blackhat = cv2.morphologyEx(resim, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow("Orjinal", resim)
cv2.imshow("Daraltma (Erosion)", daraltma)
cv2.imshow("Genisleme (Dilation)", genisleme)


cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradyan", gradyan)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()