class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto (self, produto):
        self.produtos.append(produto)

    def lista_produtos (self):
        for produto in self.produtos:
        print(produto.nome, produto.valor)
    
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
print(f'R$ {carrinho.soma_total():.2f}')


# Outro exemplo

# Usando o arquivo classes
from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já esta falando')
            return
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print (f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print (f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer. ')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = Pessoa('Thiago', 38)
p2 = Pessoa('João', 45)
p1.falar('POO')
p2.falar('filmes')
print(p2.get_ano_nascimento())