import cv2
faceCascades = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
color = (255,0,255)

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)
count = 0

while True:
    success, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascades.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.putText(img, "face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        result = img[y:y + h, x:x + w]
        cv2.imshow("Result", result)
        cv2.imwrite("FACE/No_" + str(count) + ".jpg", result)
        count += 1
    cv2.imshow("IMG", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()