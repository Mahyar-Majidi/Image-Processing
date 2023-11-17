import cv2
from matplotlib import pyplot as plt

img = cv2.imread("images/RGB.jpg", 1)

# resize the pic two times bigger that original picture
resize = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("original pic", img)
cv2.imshow("resized pic", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# split the picture channels
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
