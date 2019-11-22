import cv2
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    imgYCC = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('YCrCb Filter', imgYCC)

    _, _, Cb = cv2.split(imgYCC)

    cv2.imshow('Cb Filter', Cb)
    cv2.threshold(Cb, 102, 255, cv2.THRESH_BINARY_INV, dst=Cb)

    cv2.imshow('Cb Threshold Filter', Cb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite('finalframe.png', frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

