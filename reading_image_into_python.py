from skimage import io, img_as_float, img_as_ubyte

# read pic as a numpy array (0..255)
img = io.imread("images/Osteosarcoma_01.tif")
#  read pic as a float numpy array (0..255 convert into 0..1 values)
img2 = img_as_float(img)
img_8bit = img_as_ubyte(img2)
