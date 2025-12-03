import cv2
 
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 
cam = cv2.VideoCapture(0)

# 3. Ana Döngü
while True: 

    ok, kare = cam.read()
    if not ok:
        break

 
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
 
    yuzler = face.detectMultiScale(gri, 1.3, 5)

 
    for (x, y, w, h) in yuzler:
 
        cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
 
    cv2.imshow("Yuz Tespit", kare)
 
    if cv2.waitKey(1) == 27:
        break

 
cam.release()
cv2.destroyAllWindows()