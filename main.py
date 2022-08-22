# This is a sample Python script.
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Test', 'Best', 59999)
emp_2 = Employee('Easy', 'Peasy', 48888)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# emp_1.fullname()
# Employee.fullname(emp_1)
print(emp_1.fullname())