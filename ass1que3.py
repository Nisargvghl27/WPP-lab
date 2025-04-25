# Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards, etc. While this can be done with if statements, it is much shorter with lists and it is also easier to add new conversions if you use lists.

feet=float(input("Enter length in feet : "))

l1=["inches", "yards", "miles", "milimeters", "centimeters", "meters", "kilometers"]
l2=[feet*12, feet/3, feet*5280, feet*12*25.4, feet*12*2.54, (feet*12*2.54)/100, (feet*12*2.54)/(100*1000)]

print()
for i,name in enumerate(l1,1):
    print(f"{i}. convert to {name} : ")
print()
x=int(input("Enter choice: "))

print()
conversion = l2[x-1]
print(conversion)