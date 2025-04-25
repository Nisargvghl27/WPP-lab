# Sherlock and Squares
# Watson gives two integers A & B to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).
# A square integer is an integer which is the square of any integer.

import math

l = []
n = int(input("Enter number of test case : "))
for i in range(n):
    a = int(input("Enter value of first integer : "))
    b = int(input("Enter value of second integer : "))
    count = 0
    while a <= b:
        x = int(math.sqrt(a))
        if x**2 == a:
            count += 1
        a += 1
    l.append(count)

for i in l:
    print(i)