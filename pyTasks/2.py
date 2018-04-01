import numpy as np


x = np.array([1, 4, 10, 15])
y = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


A = np.array([[1, x[i], x[i]**2, x[i]**3] for i in range(4)])


print(A)


print(np.linalg.solve(A, y))
