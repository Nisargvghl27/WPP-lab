# Is Fibo
# You are given a integer, N. Write a program to determine if N is an element of the Fibonacci
# Sequence.
# The first few elements of Fibonacci sequence are 0,1,1,2,3,5,8,13...... A Fibonacci sequence is one
# where every element is a sum of the previous two elements in the sequence. The first two elements
# are 0 and 1.
# Formally:
# Fib0 = 0
# Fib1 = 1
# Fibn = Fibn-1 + Fibn-2 for all n > 1


def fibo(num, a=0, b=1):
    if num == a or num == b:
        return True
    if b > num:
        return False
    return fibo(num, b, a + b)


n = int(input("Enter any number : "))
if fibo(n):
    print("IsFibo")
else:
    print("IsNotFibo")