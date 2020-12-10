import cv2, time

# Frame Parameters
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255, 0, 255)

# Reading from the Video
cap = cv2.VideoCapture("Resources/vid.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    # if there is any images left
    if success:
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # converting to grey
        numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.2, 10)
        for (x, y, w, h) in numberPlates:    # exploring all number Plates
            cv2.rectangle(img, (x, y), (x + w, y + h),(255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("Plate Number", imgRoi)   # extracted Number Plate image from sample
            # saving the every number plates images
            cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
            cv2.putText(img, "Image  Saved", (150, 265), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2)
            #cv2.putText(img, "github:https://github.com/ajay-panchal-099",(60,310), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),)
            count += 1
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break
    cv2.imshow("Sample ", img)
# destroying frame
cap.release()
cv2.destroyAllWindows()
