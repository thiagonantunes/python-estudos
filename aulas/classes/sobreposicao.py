# Sobreposição de membros

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.getname = self.__class__.__name__

    def falar(self):
        print(f'{self.getname} está falando..')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.getname} está comprando... ')

    def falar(self):
        print('Estou em Pessoa')

class ClienteVIP(Cliente):
    def falar(self):
        Pessoa.falar(self) # Esse método chama o método falar da classe Pessoa
        print('Outra coisa qualquer') # Esse método subscreve o método falar da classe Pessoa

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.getname} está etudando... ')

c2 =ClienteVIP('Stewart', 76)
c2.falar()