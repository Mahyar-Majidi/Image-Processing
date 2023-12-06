from __future__ import print_function
import sys

import cv2 as cv
import numpy as np

img = cv.imread("images/sample/01.jpg", cv.IMREAD_GRAYSCALE)


# Expand the image to an optimal size
# The performance of a DFT is dependent of the image size. It tends to be the fastest for
# image sizes that are multiple of the numbers two, three and five. Therefore, to achieve
# maximal performance it is generally a good idea to pad border values to the image to get a
# size with such traits. The getOptimalDFTSize() returns this optimal size and we can use the
# copyMakeBorder() function to expand the borders of an image (the appended pixels are
# initialized with zero):

rows, cols = img.shape
m = cv.getOptimalDFTSize(rows)
n = cv.getOptimalDFTSize(cols)
padded = cv.copyMakeBorder(img, 0, m - rows, 0, n -
                           cols, cv.BORDER_CONSTANT, value=[0, 0, 0])


# Make place for both the complex and the real values
# The result of a Fourier Transform is complex. This implies that for each image value the
# result is two image values (one per component). Moreover, the frequency domains range is
#  much larger than its spatial counterpart. Therefore, we store these usually at least in a
# float format. Therefore we'll convert our input image to this type and expand it with
# another channel to hold the complex values:

planes = [np.float32(padded), np.zeros(padded.shape, np.float32)]
complexI = cv.merge(planes)  # Add to the expanded another plane with zeroes


# Make the Discrete Fourier Transform
# It's possible an in-place calculation (same input as output):

cv.dft(complexI, complexI)  # this way the result may fit in the source matrix

# Transform the real and complex values to magnitude
# A complex number has a real (Re) and a complex (imaginary - Im) part. The results of a
# DFT are complex numbers.
# Translated to OpenCV code:

cv.split(complexI, planes)   # planes[0] = Re(DFT(I), planes[1] = Im(DFT(I))
cv.magnitude(planes[0], planes[1], planes[0])  # planes[0] = magnitude
magI = planes[0]

# Switch to a logarithmic scale
# It turns out that the dynamic range of the Fourier coefficients is too large to be
# displayed on the screen. We have some small and some high changing values that we can't
# observe like this. Therefore the high values will all turn out as white points, while the
# small ones as black. To use the gray scale values to for visualization we can transform our
# linear scale to a logarithmic one:
# M1=log(1+M)
# Translated to OpenCV code:
matOfOnes = np.ones(magI.shape, dtype=magI.dtype)
cv.add(matOfOnes, magI, magI)  # switch to logarithmic scale
cv.log(magI, magI)

# Crop and rearrange
# Remember, that at the first step, we expanded the image? Well, it's time to throw away the
# newly introduced values. For visualization purposes we may also rearrange the quadrants
# of the result, so that the origin (zero, zero) corresponds with the image center.
magI_rows, magI_cols = magI.shape
# crop the spectrum, if it has an odd number of rows or columns
magI = magI[0:(magI_rows & -2), 0:(magI_cols & -2)]
cx = int(magI_rows/2)
cy = int(magI_cols/2)

q0 = magI[0:cx, 0:cy]         # Top-Left - Create a ROI per quadrant
q1 = magI[cx:cx+cx, 0:cy]     # Top-Right
q2 = magI[0:cx, cy:cy+cy]     # Bottom-Left
q3 = magI[cx:cx+cx, cy:cy+cy]  # Bottom-Right

tmp = np.copy(q0)               # swap quadrants (Top-Left with Bottom-Right)
magI[0:cx, 0:cy] = q3
magI[cx:cx + cx, cy:cy + cy] = tmp

tmp = np.copy(q1)               # swap quadrant (Top-Right with Bottom-Left)
magI[cx:cx + cx, 0:cy] = q2
magI[0:cx, cy:cy + cy] = tmp

# Normalize
# This is done again for visualization purposes. We now have the magnitudes,
# however this are still out of our image display range of zero to one. We normalize our
# values to this range using the cv::normalize() function.

# Transform the matrix with float values into a
cv.normalize(magI, magI, 0, 1, cv.NORM_MINMAX)

cv.imshow("Input Image", img)    # Show the result
cv.imshow("spectrum magnitude", magI)
cv.waitKey(0)
cv.destroyAllWindows()
