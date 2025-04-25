# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).

import numpy as np

N = 10
carpt = np.random.rand(N, 2) * 10     # cartesian point

r = np.sqrt(carpt[:, 0]**2 + carpt[:, 1]**2)
theta = np.arctan2(carpt[:, 1], carpt[:, 0])

popt = np.column_stack((r, theta))     # polar point

print("Cartesian Coordinates:\n", carpt)
print("\nPolar Coordinates:\n", popt)