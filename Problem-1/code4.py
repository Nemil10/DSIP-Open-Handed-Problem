import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-2, 11)

u = lambda x: (x >= 0).astype(int)

x = u(n) - u(n-3) - 5*u(n-7)

plt.stem(n, x)
plt.title("x[n] = u(n) - u(n-3) - 5u(n-7)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()