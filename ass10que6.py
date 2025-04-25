# The bisection method is a technique for finding solutions (roots) to equations with a single
# unknown variable. Given a polynomial function f, try to find an initial interval off by
# random probe. Store all the updates in an Numpy array. Plot the root finding process using
# the matplotlib/pyplot library.

import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return x**3 - 5*x**2 + 2

def find_initial_interval(func, lower=-10, upper=10, max_iter=1000):
    for _ in range(max_iter):
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
        if func(a) * func(b) < 0:
            return a, b
    raise Exception("Couldn't find an initial interval with a sign change.")

a, b = find_initial_interval(f)
print("Initial interval: [{:.4f}, {:.4f}]".format(a, b))

n_iterations = 20
midpoints = []

for i in range(n_iterations):
    c = (a + b) / 2.0
    midpoints.append(c)

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

midpoints_array = np.array(midpoints)

print("\nMidpoints (updates) of each iteration:")
for i, midpoint in enumerate(midpoints_array, 1):
    print("Iteration {}: {:.6f}".format(i, midpoint))

plt.figure(figsize=(10, 6))
plt.plot(range(1, n_iterations + 1), midpoints_array, marker='o', linestyle='-', color='b')
plt.title("Bisection Method Root Finding Process")
plt.xlabel("Iteration")
plt.ylabel("Midpoint Estimate")
plt.grid(True)
plt.show()
