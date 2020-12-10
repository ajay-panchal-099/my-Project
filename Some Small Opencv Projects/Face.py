import cv2
import time

video = cv2.VideoCapture(0)


num = 0
while True:
    num = num + 1
    check, frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("capture ", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



print(num)
video.release()
cv2.destroyAllWindows()
