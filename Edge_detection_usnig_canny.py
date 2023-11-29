import cv2
import numpy as np

img = cv2.imread("images/sample/01.png", 0)


canny_edge = cv2.Canny(img, 50, 80)


# Autocanny
sigma = 0.3
median = np.median(img)

# apply automatic Canny edge detection using the compute median
lower = int(max(0, (1.0 + sigma) * median))
# lower threshold is sigma % lower than median
# if the value is below than 0 then take 0 a the value

upper = int(min(255, (1.0 + sigma) * median))
# Upper threshold is sigma% higher that median
# if the value is larger than 255 then take 255 a the value
auto_canny = cv2.Canny(img, lower, upper)

cv2.imshow("Canny", canny_edge)
cv2.imshow("Auto Canny", auto_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
