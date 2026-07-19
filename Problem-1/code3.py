import matplotlib.pyplot as plt
import numpy as np

# Define the range and number of points
n = np.linspace(-2, 2, 200)

# Define the piecewise function
x = np.piecewise(
    n,
    [n < -1, (-1 <= n) & (n <= 1), n > 1],
    [-2, lambda n: 2 * n, 2],
)

# Plotting the signal
plt.plot(n, x)
plt.xlim(-2, 2)
plt.ylim(-3, 3)
plt.title("signal")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid()
plt.show()