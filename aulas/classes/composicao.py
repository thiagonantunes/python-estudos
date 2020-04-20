    class Cliente:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            self.endereco = []

        def inserir_endereco(self, cidade, estado):
            self.endereco.append(Endereco(cidade, estado))  # Composição aqui
        
        def lista_endereco(self):
            print(self.nome)
            for end in self.endereco:
                print(end.cidade, end.estado)
            print()

    class Endereco:
        def __init__(self, cidade, estado):
            self.cidade = cidade
            self.estado = estado


    c1 = Cliente('Thiago', 37)
    c1.inserir_endereco('Americana', 'SP')
    c1.inserir_endereco('São Paulo', 'SP')
    c1.inserir_endereco('Salvador', 'Ba')

    c2 = Cliente('Igor', 44)
    c2.inserir_endereco('Adamantina','MG')
    c2.inserir_endereco('Campo Grande','MS')

    c1.lista_endereco()
    c2.lista_endereco()


