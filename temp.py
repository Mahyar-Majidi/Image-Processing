
import cv2
import numpy as np
import matplotlib.pylab as plt

# x = np.arange(256)  # generate values from 0 to 255 (our image size)
# y = np.sin(np.pi * x / 20)  # calculate sine of x values
# # Divide by a smaller number above to increase the frequency.
# # y += max(y)

# img = np.array([[y[j] * 127 for j in range(256)] for i in range(256)],
#                dtype=np.uint8)  # create 2-D array of sine-wave

# plt.plot(x, y)
# plt.show()


a = np.float32(np.array([5, 2, 5, 8, 6]))
b = np.float32(np.array([5, 4, 5, 7, 6]))

d = cv2.magnitude(a, b)
print(a)
print(b)
print(d)
