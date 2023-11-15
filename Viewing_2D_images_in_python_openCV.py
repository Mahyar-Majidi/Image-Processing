from skimage import io
import cv2

img = io.imread("images/Osteosarcoma_01.tif")

gray_img = cv2.imread("images/Osteosarcoma_01.tif", 0)
color_img = cv2.imread("images/Osteosarcoma_01.tif", 1)

img_RGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

cv2.imshow("Pic from skimage import", img_RGB)
cv2.imshow("Color pic from openCV", color_img)
cv2.imshow("Gray pic from openCV", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
