# EXPRESSÃO CONDICIONAL COM OPERADOR OR

nome = input('Digite seu nome: ')
if nome:
    print(f'Nome: {nome}')
else:
    print('Você não digitou nada')

# código acima pode ser escrito da seguinte forma:
print(nome or 'Você não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Thiago'

variavel = a or b or c or d or e or f or g

print(variavel)  # irá retornar o 1º valor verdadeiro