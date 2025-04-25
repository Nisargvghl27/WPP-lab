# Maximizing XOR
# Given two integers: L and R, Find the maximal values of A xor B given, L <= A <= B <= R

l = int(input("Enter an first integer : "))
r = int(input("Enter an last integer : "))

l1 = []
for i in range(l, r + 1):
    for j in range(i, r + 1):
        l1.append(i ^ j)

print(max(l1))