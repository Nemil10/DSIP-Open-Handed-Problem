import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 7)
x = [1, 2, 3, 3, 2, 1, 0]

plt.step(n, x, where="post")
plt.xlim(0, 6)
plt.ylim(0, 4)
plt.title("signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()