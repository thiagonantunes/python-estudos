#MAP / FILTER

produtos = [
    {'nome':'p1', 'preço': 13},
    {'nome':'p2', 'preço': 55.55},
    {'nome':'p3', 'preço': 5.59},
    {'nome':'p4', 'preço': 22},
    {'nome':'p5', 'preço': 81.23},
    {'nome':'p6', 'preço': 5.70},
    {'nome':'p7', 'preço': 10.90},
    {'nome':'p8', 'preço': 88.92},
    {'nome':'p9', 'preço': 12},
    {'nome':'p10', 'preço': 2.90},
]

pessoas = [
    {'nome': 'Luiz', 'idade': 32},
    {'nome': 'Eduarda', 'idade': 43},
    {'nome': 'Joana', 'idade': 65},
    {'nome': 'Lucas', 'idade': 14},
    {'nome': 'Felipe', 'idade': 17},
    {'nome': 'Maria', 'idade': 19},
    {'nome': 'Júlia', 'idade': 25},
    {'nome': 'Diniz', 'idade': 32},
    {'nome': 'Max', 'idade': 23},
    {'nome': 'Eduardo', 'idade': 59},
]

lista = [1,2,3,4,5,6,7,8,9,10]

#nova_lista = map(lambda x: x * 2, lista)
#nova_lista = [x * 2 for x in lista]
#print(list(nova_lista))


def aumenta(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p
novo_produto = map(aumenta, produtos)
for produto in novo_produto:
    print(produto)


def velho(pessoa):
    if pessoa['idade'] > 35:
        return True

velho = filter(velho, pessoas)

for idoso in velho:
    print(idoso)

print()
nova_lista = filter(lambda x: x['preço'] > 50, produtos)

#nova_lista = [x for x in lista if x > 5]  #List comprehension
#nova_lista = filter(lambda x: x >5, lista)

for produto in nova_lista:
    print(produto)


x = chr(8594)
print(f'Thiago {x} Nonato')
estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']
list(enumerate(estacoes, start=1))

# FUNÇÃO FILTER
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False
filteredVowels = filter(filterVowels, alphabets)

for vowel in filteredVowels:
    print(vowel)



lista = [1,2,4,5,6,9,10]
r = map(lambda x: x*x*x, lista)
y = [x*x*x for x in lista]
print(list(r))
print(y)
