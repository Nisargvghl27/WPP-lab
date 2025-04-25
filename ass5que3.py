# Bigger is Greater
# Given a word w, rearrange the letters of w to construct another word s in such a way that s is
# lexicographically greater than w.

from itertools import permutations

n = int(input("Enter number of test case : "))
l = []
for i in range(n):
    str = input("Enter any string : ")
    str1 = str.lower()
    l1 = sorted(set("".join(i) for i in permutations(str1)))
    index = l1.index(str1)
    str2 = l1[index + 1] if index + 1 < len(l1) else "no answer"
    l.append(str2)
    l1.clear()

for i in l:
    print(i)