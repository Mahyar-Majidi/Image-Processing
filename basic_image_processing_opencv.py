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

#  instead of lines above you can use these lines below
b, g, r = cv2.split(img)

# after that, process on each channel, you can merge those channel together again
img_merge = cv2.merge((b, g, r))

# show the split channel
cv2.imshow("Blue red ", b)
cv2.imshow("Merged img ", img_merge)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_2 = cv2.imread("images/Osteosarcoma_01.tif")
# this filter used for edges detection in pic by min and max values
edges = cv2.Canny(img_2, 100, 200)

cv2.imshow("Original picture", img_2)
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
