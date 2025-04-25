# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.

import numpy as np
a=np.zeros(shape=(8,8))

k=0
j=0
for i in range(8):
    if(a[i][j]==1):
        i+=1
    else:
        if(k>3):
            a[i][(2*k+2)%8]=1
            k+=1
        else:
            a[i][(2*k+1)%8]=1
            k+=1
print(a)            