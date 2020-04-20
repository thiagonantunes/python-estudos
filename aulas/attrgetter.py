"""
Função attrgetter do módulo operator pode ser usado no lugar da função lambda para ordenar uma lista.
"""

from operator import attrgetter

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'

    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee('Carl', 37, 7000)
e2 = Employee('Sarah', 29, 8000)
e3 = Employee('John', 43, 9000)

employees = [e1, e2, e3]

# x = lambda e: e.name

s_employees = sorted(employees, key=attrgetter('age'))
# print(s_employees)
print(e1)