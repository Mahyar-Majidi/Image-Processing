# Unsharp mask
# unsharpened image = original + amount * (original - blurred)
# Note: if you want apply some skimage filter on any picture, you should convert it to float
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
from matplotlib import pyplot as plt

img = img_as_float(io.imread("images/sample/02.jpg", as_gray=True))
gaussian_img = gaussian(img, sigma=4, mode='constant', cval=0.0)

img2 = (img - gaussian_img) * 2
img3 = img + img2

plt.imshow(img, cmap="gray")
plt.show()
plt.imshow(img2, cmap="gray")
plt.show()
plt.imshow(img3, cmap="gray")
plt.show()
