# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
# monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
# increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
# the height of the tree after N growth cycles?

l = []
case = int(input("Enter number of test case : "))
j = 0
while j != case:
    n = int(input("Enter number of growth cycles : "))
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    l.append(height)
    j += 1

for i in l:
    print(i)