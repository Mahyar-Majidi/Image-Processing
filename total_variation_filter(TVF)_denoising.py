import cv2
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import denoise_tv_chambolle

img = img_as_float(io.imread('images/Osteosarcoma_01_25Sigma_noise.tif'))

denoise_img = denoise_tv_chambolle(
    img, weight=0.1, eps=0.0002)

img_as_byte = img_as_ubyte(img)
denoise_img_as_8byte = img_as_ubyte(denoise_img)

original_img = cv2.cvtColor(img_as_byte, cv2.COLOR_BGR2RGB)
final_denoise_img = cv2.cvtColor(denoise_img_as_8byte, cv2.COLOR_BGR2RGB)

cv2.imshow('Original pic', original_img)
cv2.imshow('TV Filtered', final_denoise_img)
cv2.waitKey(0)
cv2.destroyWindow()
