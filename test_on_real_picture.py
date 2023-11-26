import cv2
from skimage.filters import median
from skimage.morphology import disk
from skimage.filters import unsharp_mask

original_pic = cv2.imread('images/sample/01.png', 0)

bilateral_picture = cv2.bilateralFilter(
    original_pic, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

median_using_cv2 = cv2.medianBlur(original_pic, 5)
median_using_skimage = median(original_pic, disk(3), mode='constant', cval=0.0)

unsharped_img = unsharp_mask(median_using_skimage, radius=3, amount=2)

cv2.imshow('Original picture', original_pic)
cv2.imshow('Median picture using cv2', median_using_cv2)
cv2.imshow('Median picture using skimage', median_using_skimage)
cv2.imshow('unsharped picture cv2', unsharped_img)
cv2.imshow('bilateral picture', bilateral_picture)
cv2.waitKey(0)
cv2.destroyAllWindows()
