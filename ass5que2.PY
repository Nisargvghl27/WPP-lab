# Halloween Party
# Alex is attending a Halloween party with his girlfriend Silvia. At the party, Silvia spots a giant
# chocolate bar. If the chocolate can be served as only 1*1 sized pieces and Alex can cut the
# chocolate bar exactly K times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?


def div(a):
    x = a // 2
    y = a - x
    return x * y


n = int(input("Enter number of test case : "))
print(f"Enter {n} number saperated by space : ")

while 1:
    l = input().split()
    if len(l) != n:
        print(f"Please enter {n} numbers.")
    else:
        break

l1 = []
for i in l:
    l1.append(div(int(i)))

for i in l1:
    print(i)