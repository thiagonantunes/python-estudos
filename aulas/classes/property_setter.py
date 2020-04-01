class Employee:

    def __init__ (self, first, last):
      self.first = first
      self.last = last
      # self.email = f'{first}.{last}@company.com'  #first + '.' + last + '@email.com'

  @property
  def email(self):
      return f'{self.first}.{self.last}@company.com'

  @property
  def fullname(self):
      return f'{self.first} {self.last}'

  @fullname.setter
  def fullname(self, name):
      first, last = name.split(' ')
      self.first = first
      self.last = last

  @fullname.deleter
  def fullname(self):
      print('Delete name!')
      self.first = None
      self.last = None

emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Corey Schafer'

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname


#  Outro exemplo

class Produtos:
    def __init__ (self, produto, valor):
        self.produto = produto
        self.valor = valor

    def desconto(self, porcentagem):
        self.valor = self.valor - (self.valor * (porcentagem / 100))

    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, nome):
        self._produto = nome.capitalize()

    @property   #Getter
    def valor(self):
        return self._valor

    @valor.setter   #Setter
    def valor(self, valor):
        if isinstance(valor, str): # verifica se valor é string
        valor = float(valor.replace('R$', ''))
        self._valor = valor

p1 = Produtos('calça', 80)
print(p1.valor)
p1.desconto(10)
print(p1.produto, p1.valor)

p2 = Produtos('caneca', 'R$15.50') # caso isso aconteca com o valor, será feito @property (getter/setter)
print(p2.valor)
p2.desconto(20)
print(p2.produto, p2.valor)
