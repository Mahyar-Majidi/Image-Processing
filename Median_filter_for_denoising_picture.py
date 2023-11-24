import cv2
from skimage.filters import median
from skimage.morphology import disk

img_gaussian_noise = cv2.imread('images/Osteosarcoma_01_25Sigma_noise.tif', 0)
img_salt_pepper_noise = cv2.imread(
    'images/Osteosarcoma_01_8bit_salt_pepper.tif', 0)

img = img_gaussian_noise
median_using_cv2 = cv2.medianBlur(img, 3)

median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)

cv2.imshow('Original', img)
cv2.imshow('cv2 median', median_using_cv2)
cv2.imshow('Using skimage median', median_using_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
