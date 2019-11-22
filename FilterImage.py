import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("SkystoneImages/IMG_20191121_154739082_HDR.jpg")
imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

_, _, Cb = cv2.split(imgYCC)

# Threshold Cb channel
cv2.threshold(Cb, 102, 255, cv2.THRESH_BINARY_INV, dst=Cb)

# HSV Operations
lower_yellow = np.array([5, 90, 90])
upper_yellow = np.array([30, 255, 255])

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(imgHSV, lower_yellow, upper_yellow)

plt.figure(1)
plt.imshow(Cb)

plt.figure(2)
plt.imshow(mask)

plt.figure(3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

plt.show()
