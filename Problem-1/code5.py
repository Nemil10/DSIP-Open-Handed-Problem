import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-3, 4)

x = np.zeros(len(n))
x[n == 0] = 1
x[n == 1] = 4
x[n == -1] = 5

plt.stem(n, x)
plt.title("x[n]=delta(n)+4delta(n-1)+5delta(n+1)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()