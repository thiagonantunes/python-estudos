class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # Será agregado valor aqui

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
