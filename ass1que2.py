# Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros, the largest number of zeros in a row. For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random
l=[random.randint(0,1) for i in range(100)]
current=0
count=0
for i in l:
    if i==0:
        current+=1
    else:
        current=0
    count=max(current,count)
    
print(l)
    
print(count)