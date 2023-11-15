from skimage import io
import matplotlib.pyplot as plt

img = io.imread("images/Osteosarcoma_01.tif", as_gray=True)

# plt.imshow(img, cmap="hot")
#  the brightest pixel get more read value and the darkness less
# for other custom color you can search in google "pyplot colormap"

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(img, cmap='hot')
ax1.title.set_text("1st")

ax1 = fig.add_subplot(2, 2, 2)
ax1.imshow(img, cmap='jet')
ax1.title.set_text("2st")

ax1 = fig.add_subplot(2, 2, 3)
ax1.imshow(img, cmap='gray')
ax1.title.set_text("3st")

ax1 = fig.add_subplot(2, 2, 4)
ax1.imshow(img, cmap='nipy_spectral')
ax1.title.set_text("4st")

plt.show()
