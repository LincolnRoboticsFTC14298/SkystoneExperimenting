import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Our operations on the frame come here
    # lower_yellow = np.array([10, 0, 20])
    # upper_yellow = np.array([35, 250, 255])

    lower_yellow = np.array([10, 140, 140])
    upper_yellow = np.array([30, 255, 255])

    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(imgHSV, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('HSV Yellow Filter', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite('finalframe.png', frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

