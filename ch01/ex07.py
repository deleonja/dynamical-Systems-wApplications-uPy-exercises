# Author: José Alfredo de León
# Date: 19.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.7

import numpy as np
import matplotlib.pyplot as plt
import math

# (a) y = 3x^3 + 2x^2 − 5
def a(x):
    return 3*x**3 + 2*x**2 - 5

# y = e^(−x) , for −5 ≤ x ≤ 5
def b(x):
    return np.exp(-x**2)

x = np.arange(-5, 5, 0.1)

y1 = a(x)
y2 = b(x)

plt.plot(x, y1, '-k', lw=0.8, label=r"$f(x)=3x^3+2x^2-5$")
plt.plot(x, y2, '-b', lw=0.8, label=r"$f(x)=e^{-x^2}$")
plt.xlim(-5, 5)
plt.ylim(-10, 10)
plt.grid('--k', lw=0.1)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.legend()
plt.show()
