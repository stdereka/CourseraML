from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def h(x):
    return f(x).astype(int)


print(optimize.minimize(h, np.array(30), method='BFGS'))
print("------------------------------------------------------------------")
print(optimize.differential_evolution(h, [(1, 30)]))

X = np.arange(1, 30, 0.01)
plt.plot(X, h(X))

plt.show()
