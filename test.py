import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 1000)
y = np.cos(x)
plt.plot(x, y)
plt.xlim((-2*np.pi, 2*np.pi))
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(x)")
plt.show()