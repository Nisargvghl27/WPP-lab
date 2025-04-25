# Create a class "employee" with attributes name and salary. Implement overloaded operators + and - to combine and compare employees based on their salaries.
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, e2):
        totalsalary = self.salary + e2.salary
        return totalsalary

    def __sub__(self, e2):
        totalsalary = self.salary - e2.salary
        return totalsalary


e1 = employee("ABC", 100000)
e2 = employee("XYZ", 120000)

combinesalary = e1 + e2
differencesalary = e1 - e2

print(f"combine salary of Employee {e1.name} and {e2.name} : {combinesalary}")
print(f"difference between the salary : {abs(differencesalary)}")