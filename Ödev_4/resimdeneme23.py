import cv2
import numpy as np

resim = cv2.imread("newyork.jpg")

orb = cv2.ORB_create()

kp, des = orb.detectAndCompute(resim, None)

sonuc = cv2.drawKeypoints(resim, kp, None, color=(0, 255, 0))

cv2.imshow("Orjinal", resim)
cv2.imshow("ORB Noktalari", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()
