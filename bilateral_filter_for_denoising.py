import cv2

img_gaussian_noise = cv2.imread('images/Osteosarcoma_01_25Sigma_noise.tif', 0)

img = img_gaussian_noise

bilateral_using_cv2 = cv2.bilateralFilter(
    img, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

#   d - diameter of each pixel neighborhood used during filtering
#   sigmaColor - Sigma of gray/color space.
#   sigmaColor - Large value means farther pixels influence each other (as long the colors are close enough)

cv2.imshow('Original', img)
cv2.imshow('CV2 bilateral', bilateral_using_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
