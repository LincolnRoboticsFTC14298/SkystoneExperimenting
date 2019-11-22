import cv2
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

# From this tutorial https://realpython.com/python-opencv-color-spaces/
# Start with reading the image using OpenCV
skystone_image = cv2.imread('InnerSkystone.png')

# Since plt displays in BGR, we need to convert the RGB image to BGR
skystone_image = cv2.cvtColor(skystone_image, cv2.COLOR_RGB2BGR)

# plt.imshow(skystone_image)
# plt.show()

# Turns the 2D skystone_image array into a large array with 3 values each inner array.
pixel_colors = skystone_image.reshape((np.shape(skystone_image)[0] * np.shape(skystone_image)[1], 3))
norm = colors.Normalize(vmin=- 1., vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

YCrCb_skystone = cv2.cvtColor(skystone_image, cv2.COLOR_BGR2YCR_CB)
# Split separates the channels
Y, Cr, Cb = cv2.split(YCrCb_skystone)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

# Scatter plot
# Flatten() turns 2D array of values into 1D array
axis.scatter(Y.flatten(), Cr.flatten(), Cb.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Y")
axis.set_ylabel("Cr")
axis.set_zlabel("Cb")
plt.show()
