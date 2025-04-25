# Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.


class password_manager:
    def __init__(self):
        self.old_password = ["hello123", "abcd754", "xyz4365"]

    def get_password(self):
        return self.old_password[-1]

    def set_password(self, new):
        if new not in self.old_password:
            self.old_password.append(new)
            print("Password is changed")
        else:
            print("Password is alredy used before")

    def is_correct(self, check):
        return check == self.get_password()


nv = password_manager()
while True:
    print()
    print("1. get current password.")
    print("2. set new password.")
    print("3. check current password is correct or not.")
    print("0. exit")
    try:
        choice = int(input("Enter any choice : "))
        print()
        if choice == 1:
            print("current password is", nv.get_password())
        elif choice == 2:
            new = input("Enter new password : ")
            nv.set_password(new)
        elif choice == 3:
            check = input("Enter password to check : ")
            print("Entered password is", nv.is_correct(check))
        elif choice == 0:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice, Please enter an integer")