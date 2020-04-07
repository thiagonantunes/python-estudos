class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto (self, produto):
        self.produtos.append(produto)

    def lista_produtos (self):
        print('Itens no carrinho')
        for produto in self.produtos:
            print(f'--> {produto.nome:<10}R$ {produto.valor:>6.2f}')
    
    def soma_total(self):
        total = sum(produto.valor for produto in self.produtos)
        return total

class Produto:
    def __init__ (self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Calça', 120)
p3 = Produto('tenis', 340)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()
print(f'{carrinho.soma_total():>23.2f}')


# Outro exemplo

# Usando o arquivo classes
from datetime import datetime

class Person:

    ano = 2020
    # actual_year = datetime.strftime(datetime.now(), '%Y')
    actual_year = int(datetime.today().year)

    def __init__(self, name, age, speaking=False, eating=False):
        self.name = name
        self.age = age
        self.speaking = speaking
        self.eating = eating

    def speak(self, subject):
        if self.eating:
            print(f'{self.name} cant speak while eating')
            return

        if not self.speaking:
            print(f'{self.name} is speaking about {subject}')
            self.speaking = True
            return
        print(f'{self.name} is already speaking')

    def eat(self, food):
        if self.speaking:
            print(f'{self.name} cant eat while speaking')
            return

        if self.eating:
            print(f'{self.name} is already eating')
            return
        print(f'{self.name} is eating {food}')
        self.eating = True
        return

    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return
        print (f'{self.name} stop eating')
        self.eating = False
        return

        if self.speaking:
            print(f'{self.name} cant eat while speaking')
            return

    def stop_speak(self):
        if not self.speaking:
            print(f'{self.name} is not speaking')
            return
        print (f'{self.name} stop speaking')
        self.speaking = False
        return

        if self.eating:
            print(f'{self.name} cant speak while eating')
            return

    @property
    def birth_year(self):
        return Person.actual_year - self.age

    @classmethod
    def test(cls, year):
        return cls.ano - year

p1 = Person('John', 26)
print(p1.birth_year)
print(Person.test(1982))
    