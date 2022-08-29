# This is a sample Python script.
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Test', 'Best', 59999)
emp_2 = Employee('Easy', 'Peasy', 48888)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# emp_1.fullname()
# Employee.fullname(emp_1)
# print(emp_1.fullname())

# print(Employee.__dict__)

# emp_1.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount
# Employee.raise_amount

print(Employee.num_of_emps)