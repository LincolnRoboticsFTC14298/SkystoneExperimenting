import cv2


pic = cv2.imread("InnerSkystone.png")
pic_hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

h_range = [pic_hsv[0, 0][0], pic_hsv[0, 0][0]]
s_range = [pic_hsv[0, 0][1], pic_hsv[0, 0][1]]
v_range = [pic_hsv[0, 0][2], pic_hsv[0, 0][2]]

height = pic_hsv.shape[0]
width = pic_hsv.shape[1]

for col in range(height):
    for row in range(width):
        pixel = pic_hsv[col, row]
        # Sees if h channel of pixel is new max or min
        if pixel[0] < h_range[0]:
            h_range[0] = pixel[0]

        if pixel[0] > h_range[1]:
            h_range[1] = pixel[0]

        # Sees if s channel of pixel is new max or min
        if pixel[1] < s_range[0]:
            s_range[0] = pixel[1]

        if pixel[1] > s_range[1]:
            s_range[1] = pixel[1]

        # Sees if v channel of pixel is new max or min
        if pixel[2] < v_range[0]:
            v_range[0] = pixel[2]

        if pixel[2] > v_range[1]:
            v_range[1] = pixel[2]

print(h_range)
print(s_range)
print(v_range)
