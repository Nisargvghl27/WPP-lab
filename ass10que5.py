# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).

import numpy as np

def fs(arr):
    arr = np.array(arr, dtype=str)
    center = np.char.center(arr, 15, fillchar='_')
    ljust = np.char.ljust(arr, 15, fillchar='_')
    rjust = np.char.rjust(arr, 15, fillchar='_')
    return center, ljust, rjust

arr = np.array(["apple", "banana", "cherry", "date"])
center, ljust, rjust = fs(arr)

print("center:")
print(center)
print("\nLeft Justified:")
print(ljust)
print("\nRight Justified:")
print(rjust)