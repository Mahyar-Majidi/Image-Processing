import cv2
import numpy as np
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma


img = img_as_float(
    io.imread('images/Osteosarcoma_01_25Sigma_noise.tif', as_gray=False))

sigma_est = np.mean(estimate_sigma(img, multichannel=True))

denoise_img = denoise_nl_means(
    img, h=1.15 * sigma_est,
    fast_mode=True,
    patch_size=5,
    patch_distance=3,
    multichannel=True)

img_as_byte = img_as_ubyte(img)
denoise_img_as_8byte = img_as_ubyte(denoise_img)

original_img = cv2.cvtColor(denoise_img_as_8byte, cv2.COLOR_BGR2RGB)
final_denoise_img = cv2.cvtColor(denoise_img_as_8byte, cv2.COLOR_BGR2RGB)

cv2.imshow("Original", original_img)
cv2.imshow("NLM Filtered", final_denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
