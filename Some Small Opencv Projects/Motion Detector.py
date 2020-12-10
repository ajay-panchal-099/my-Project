# step 1 - capture first frame
# step 2 - capture other frame
# step 3 - calculate the difference in frisr and other frame
#  step 4 - define threshold
# step 5 -   define boarders

import cv2
from sendMail import send_mail
from datetime import datetime

first_frame = None
video = cv2.VideoCapture(0)
count = 0
photos = []
time1 = datetime.now()
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # first frame
    if first_frame is None:
        first_frame = gray
        continue

    # calculate difference
    delta_frame = cv2.absdiff(first_frame, gray)
    # define threshold
    # if threshold is < 30 convert that pixels to black otherwise white
    thresh_delta = cv2.threshold(delta_frame, 30, 225, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

    # define boarders or contours

    (cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 25000:  # remove noises
            continue
        # define rectangle
        count = count + 1
        path = "Capture/ph_" + str(count) + ".jpg"
        cv2.imwrite(path, frame)
        # photos.append(path)
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('frame', frame)
    """
     cv2.imshow('gray', gray)
     cv2.imshow('delta', delta_frame)
     cv2.imshow('thresh ', thresh_delta)
    """
    """if len(photos) > 100 :
        send_mail(photos[0])
        photos.clear()
    """
    """time2 = datetime.now()
    diff = time2 - time1
    if  diff.total_seconds() > 15:
        send_mail(photos[:5])
        photos.clear()
        time1 = time2
        """

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
