# A magic square is an N×N grid of numbers in which the entries in each row, column and
# main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
# N=4, 5, 6, 7, 8

import numpy as np

def generate(n):
    if n % 2 == 1:
        return oddsquare(n)
    elif n % 4 == 0:
        return doublyevensquare(n)
    else:
        return singlyevensquare(n)

def oddsquare(n):
    magic = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n*n + 1):
        magic[i, j] = num
        i_new, j_new = (i - 1) % n, (j + 1) % n
        if magic[i_new, j_new]:
            i = (i + 1) % n
        else:
            i, j = i_new, j_new
    return magic

def doublyevensquare(n):
    magic = np.arange(1, n*n + 1).reshape(n, n)
    mask = np.ones((n, n), dtype=bool)

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                mask[i, j] = False

    magic[~mask] = n*n + 1 - magic[~mask]
    return magic

def singlyevensquare(n):
    half_n = n // 2
    mini_magic = oddsquare(half_n)
    magic = np.zeros((n, n), dtype=int)
    add = [0, 2, 3, 1]
    for i in range(half_n):
        for j in range(half_n):
            for k in range(4):
                row = i + (k // 2) * half_n
                col = j + (k % 2) * half_n
                magic[row, col] = mini_magic[i, j] + add[k] * half_n * half_n

    num_cols_left = (n - 2) // 4
    num_cols_right = num_cols_left

    for i in range(half_n):
        for j in range(n):
            if j < num_cols_left or j >= n - num_cols_right or j == num_cols_left:
                if not (j == 0 and i == num_cols_left):
                    magic[i, j], magic[i + half_n, j] = magic[i + half_n, j], magic[i, j]

    return magic

for N in range(4, 9):
    print(f"Magic Square (N={N}):\n{generate(N)}\n")
