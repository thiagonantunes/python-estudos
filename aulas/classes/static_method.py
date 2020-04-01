class Employee:

  num_of_emps = 0
  raise_amount = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company.com'  #first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
  
  def fullname(self):
    return f'{self.first} {self.last}'

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  def __repr__(self):
    return f"Employee('{self.first}','{self.last}', {self.pay})"   #"Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

  def __str__(self):
    return f'{self.fullname()} - {self.email}'

  def __len__ (self):
    return len(self.fullname())

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

  def __add__ (self, other):
    return self.pay + other.pay

class Developer(Employee):  #Subclasse
  raise_amount = 1.1
  def __init__ (self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang

class Manager(Employee):  #Subclasse
  def __init__ (self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.empolyees:
      self.employees.append(emp)
  
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
  
  def print_emps(self):
    for emp in self.employees:
      print('-->', emp.fullname())

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Thiago', 'Antunes', 6000,)
dev_1 = Developer('Smith', 'Will', 8000, 'JavaScript')
dev_2 = Developer('Thiago', 'Antunes', 6000, 'Java')
mngr1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])

# emp_string_1 = 'Rod-Stewart-5000'
# new_emp_1 = Employee.from_string(emp_string_1)
# print(new_emp_1.email)
# print(emp_1.__len__())
# print(emp_1 + emp_2)
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__str__())
# print(emp_1.__repr__())
# print(issubclass(Developer, Manager))
# print(isinstance(mngr1, Employee))
# print(mngr1.email)
# mngr1.remove_emp(dev_2)
# mngr1.print_emps()
# print(dev_1.email)
# print(dev_1.prog_lang)
# print(emp_1.email)
# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))
# emp_3 = Employee('Test', 'User', 7000)
# emp_string_1 = 'John-Doe-7000'
# print(new_emp_1.email)
# Employee.set_raise_amount(1.25)
# emp_1.raise_amount = 1.55
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.pay)
# emp_1.raise_amount = 1.15
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.fullname(emp_1))
# print(emp_1.fullname())
# print(Employee.num_of_emps)
# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))
# print(len(emp_1))