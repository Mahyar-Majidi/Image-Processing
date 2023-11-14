from matplotlib import pyplot as plt


def distance_enq(u, a):
    return lambda t: u*t + ((1 / 2) * a * t ** 2)


time = []
dist = []
for t in range(0, 22, 2):
    d = distance_enq(5, 10)(t)
    time.append(t)
    dist.append(d)

plt.plot(time, dist)
plt.show()
