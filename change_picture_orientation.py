from skimage import io
from matplotlib import pyplot as plt

img = io.imread("images/monalisa.jpg", as_gray=True)
img2 = img.T
plt.imshow(img)
# change the row and column in picture
plt.imshow(img2)
plt.show()
