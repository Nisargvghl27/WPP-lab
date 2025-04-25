# You are given a number N, you need to print the number of positions where digits exactly divides N.

n = int(input("Enter number of checks : "))
l1 = []
for i in range(n):
    l = []
    size = 0
    num = input("Enter any number : ")
    for i in num:
        l.append(int(i))
        size += 1

    count = 0
    for i in range(size):
        if int(num) % l[i] == 0:
            count += 1
        else:
            continue

    l1.append(count)

for i in l1:
    print(i)
