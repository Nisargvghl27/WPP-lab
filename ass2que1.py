# Write a program that asks the user to enter a word and then capitalizes every other letter of that word.
word=input("Enter any word : ")
j=0
for i in word:
    if j%2 != 0:
        print(i.upper(),end="")
    elif i==' ':
        print(end=" ")
        j-=1
    else:
        print(i.lower(),end="")
    j+=1