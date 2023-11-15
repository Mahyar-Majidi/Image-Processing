from skimage import io, filters, img_as_ubyte
from matplotlib import pyplot as plt
import cv2
import tifffile

img = io.imread("images/Osteosarcoma_01.tif")

gaussian_img = filters.gaussian(img, sigma=3)
gaussian_img_8bit = img_as_ubyte(gaussian_img)
io.imsave("images/export/save_using_skimage.tif", gaussian_img_8bit)


gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite("images/export/save_using_openCV.jpg", gaussian_img_8bit_RGB)

plt.imsave("images/export/save_using_pyplot.jpg", gaussian_img)


tifffile.imwrite("images/export/save_using_tifffile.tiff", gaussian_img_8bit)
