class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nameclass = self.__class__.__name__

    def falar(self)  :
        print(f'{self.nameclass} falando')

class Cliente(Pessoa):
    def comprar(self)  :
        print(f'{self.nameclass} comprando')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nameclass} estudando')

c1 = Cliente('John', 43)
a1 = Aluno('Smith', 37)

c1.comprar()