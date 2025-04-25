# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class bank:
    def __init__(self, amount):
        self.amount = amount

    def currentbal(self):
        print("current balance is : ", self.amount)

    def withdraw(self):
        n = int(input("Enter rupees you want to withdraw : "))
        if self.amount < n:
            print("not sufficient balance")
        else:
            self.amount -= n

    def credit(self):
        c = int(input("Enter rupees you want to deposit : "))
        self.amount += c


n = float(input("Enter balance which is already in account : "))
p = bank(n)
while 1:
    print()
    print("Welcome in Bank!!!")
    print("1. check current balance")
    print("2. withdrawal")
    print("3. Deposit")
    print("0. Exit")
    a = int(input("Enter choise : "))
    print()
    if a == 1:
        p.currentbal()
    elif a == 2:
        p.withdraw()
    elif a == 3:
        p.credit()
    elif a == 0:
        break
    else:
        print("Invalid Choise!!! Please enter valid choise.")
