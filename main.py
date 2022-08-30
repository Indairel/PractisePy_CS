
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# print(Employee.num_of_emps)

emp_1 = Employee('Test', 'Best', 59999)
emp_2 = Employee('Easy', 'Peasy', 48888)

import datetime
my_date = datetime.date(2022, 8, 28)

print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-69999'
# emp_str_2 = 'Jack-Smith-55555'
# emp_str_3 = 'Ytsy-Pytsy-40000'

# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)

# print(Employee.num_of_emps)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# emp_1.fullname()
# Employee.fullname(emp_1)
# print(emp_1.fullname())

# print(Employee.__dict__)

# emp_1.raise_amount = 1.05

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_1.raise_amount
# Employee.raise_amount