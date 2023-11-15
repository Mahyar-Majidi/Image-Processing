from matplotlib import pyplot as plt
from skimage import io

# you can go to the documentation and read about transform module
from skimage.transform import rescale, resize, downscale_local_mean

# you can go to the documentation and read about the filters
from skimage.filters import gaussian, sobel

img = io.imread("images/Osteosarcoma_01.tif", as_gray=True)

# rescale the original image into 0.25 percent of original size
im_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=True)

# resize the original image into 200 x 200
im_resize = resize(img, (200, 200), anti_aliasing=False)

# this is downscale original image
img_downscale = downscale_local_mean(img, (4, 3))

plt.imshow(img)
plt.show()

noisy_image = io.imread("images/Osteosarcoma_01_25Sigma_noise.tif")
plt.imshow(noisy_image)
plt.show()

gaussian_using_skimage = gaussian(
    noisy_image, sigma=1, mode="constant", cval=0.0)
plt.imshow(gaussian_using_skimage)
plt.show()


img_gray = io.imread("images/Osteosarcoma_01.tif", as_gray=True)
sobel_img = sobel(img_gray)
plt.imshow(sobel_img, cmap="gray")
plt.show()
