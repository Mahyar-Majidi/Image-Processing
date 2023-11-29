from skimage import io, img_as_float, img_as_ubyte
import bm3d
import cv2

img = img_as_float(
    io.imread("images/Osteosarcoma_01_25Sigma_noise.tif", as_gray=False))

BM3D_denoise_img = bm3d.bm3d(
    img, sigma_psd=0.05, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)

# img_as_byte = img_as_ubyte(img)
# denoise_img_as_8byte = img_as_ubyte(BM3D_denoise_img)

# original_img = cv2.cvtColor(img_as_byte, cv2.COLOR_BGR2RGB)
# final_denoise_img = cv2.cvtColor(denoise_img_as_8byte, cv2.COLOR_BGR2RGB)


cv2.imshow("Original", img)
cv2.imshow("Denoised", BM3D_denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
