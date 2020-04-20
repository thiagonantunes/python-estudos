import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    _total_contas = 0
    # __slots__ = ['_num', '_titular', '_saldo', '_historico']
    def __init__(self, num, titular, saldo, limite=1000):
        self.num = num
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        Conta._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return Conta._total_contas

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de: {valor}')

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.historico.transacoes.append(f'Saque de: {valor}')

    @property
    def extrato(self):
        return f"conta: {self.num}\nSaldo: {self.saldo}"
        self.historico.transacoes.append(f'Extrato - saldo de {self.saldo}')

    def transfere(self, destino, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        destino.saldo += valor
        self.historico.transacoes.append(f'Transferiu {valor} para {destino.num}')

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data abertura: {self.data_abertura}')
        print(f'Transações: ')
        for t in self.transacoes:
            print(f'--> {t}')

cli1 = Cliente('Thiago', 'Nonato', '298425948-31')
cli2 = Cliente('Simone', 'Antunes', '299243848-06')
cli3 = Cliente('Otto', 'Antunes', '123456789-06')
conta1 = Conta('123-4', cli1, 100, 500)
conta2 = Conta('456-9', cli2, 200)
conta3 = Conta('789-3', cli3, 200)
conta1.sacar(30)
conta1.transfere(conta2, 10)
conta1.depositar(90)
conta1.historico.imprime()


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
    