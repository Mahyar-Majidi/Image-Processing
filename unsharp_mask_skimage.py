from skimage import io
from skimage.filters import unsharp_mask
from matplotlib import pyplot as plt

img = io.imread("images/sample/01.png", as_gray=True)

# radius is the value of blurring
# amount is the value of multiplication factor (original - blurred) image
unsharped_img = unsharp_mask(img, radius=3, amount=2)

fig = plt.figure(figsize=(12, 12))

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text("Input Image")

ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(unsharped_img, cmap="gray")
ax2.title.set_text("Unsharped Image")

plt.show()
