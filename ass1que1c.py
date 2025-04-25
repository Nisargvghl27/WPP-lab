# The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
l1=[(chr(96+i)*i) for i in range(1,27)]
print(l1)