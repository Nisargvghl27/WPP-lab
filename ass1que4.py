# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence classes should be the original set/list.]
c1,c2,c3,c4,c5 = [],[],[],[],[]
for i in range(1,10001):
    if i%5==0:
        c5.append(i)
    elif i%5==1:
        c1.append(i)
    elif i%5==2:
        c2.append(i)
    elif i%5==3:
        c3.append(i)
    elif i%5==4:
        c4.append(i)
print("Equivalence class 1 is :",c1)
print("Equivalence class 2 is :",c2)
print("Equivalence class 3 is :",c3)
print("Equivalence class 4 is :",c4)
print("Equivalence class 5 is :",c5)