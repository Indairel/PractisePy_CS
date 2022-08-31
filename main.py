
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

class Developer(Employee):
    raise_amt = 1.1
    # pass
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps_list(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Test', 'Best', 59999, 'Python')
dev_2 = Developer('Easy', 'Peasy', 48888, 'Java')

mgr_1 = Manager('Panna', 'Sanna', 90000, [dev_1])

# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
#
# mgr_1.print_emps_list()

print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))