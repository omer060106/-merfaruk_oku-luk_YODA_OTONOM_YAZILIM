import cv2

camera=cv2.VideoCapture(0)

width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
writer = cv2.VideoWriter("kayit.mp4", fourcc, 50, (width,height))

while True:
    ret,frame=camera.read()
    writer.write(frame)
    cv2.imshow("Kayit videosu",frame)
    
    if cv2.waitKey(25) & 0xFF==27:
        break

camera.release()
writer.release()
cv2.destroyAllWindows()