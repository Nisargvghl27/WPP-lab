# The Love-Letter Mystery
# James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he
# decides to meddle with the letter. He changes all the words in the letter into palindromes.
# To do this, he follow 2 rules:
# (a) He can reduce the value of a letter. E.g. He can change ‘d’ to ‘c’ but he cannot change ‘c’ to ‘d’.
# (b) In order to form a palindrome, if he has to repeatedly reduce the value of a letters, he can do it
# until the letters becomes ‘a’. Once a letters has been changed to ‘a’, it can no longer be changed.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number
# of operations required to convert a given string into a palindrome.

l = []
n = int(input("Enter number of test case : "))
for i in range(n):
    str = input("Enter string : ")
    a, b, count = 0, len(str) - 1, 0
    while a < b:
        count += abs(ord(str[a]) - ord(str[b]))
        a, b = a + 1, b - 1
    l.append(count)

for i in l:
    print(i)