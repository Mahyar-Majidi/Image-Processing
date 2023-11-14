import numpy as np
from matplotlib import pyplot as plt

a = np.ones((200, 200))
b = np.zeros((200, 200))

plt.imshow(a, vmin=0, vmax=255)
plt.show()
