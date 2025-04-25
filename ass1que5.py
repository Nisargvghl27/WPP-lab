# You are a student in a class of 10. Your class teacher assigns you a task of entering the names of all the students in the class. You finally want to display the names given the condition that the maximum allowed characters in a name is 15. As a fun task, reverse the names and display them.

print("Enter name of Students: ")
l=[((name[0:15])[::-1]) for i in range(10) for name in [input()]]
print(l)