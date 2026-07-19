import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-3, 7)
x = np.where(n % 2 == 0, 3, 2)

plt.stem(n, x)
plt.title("signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()