#LAMBDA

lista = [
    ['p1', 13, 'c'],
    ['P2', 6, 'j'],
    ['p3', 7, 'a'],
    ['p4', 50, 'd'],
    ['p5', 8, 'e']
]

# Método usando lambda
print(sorted(lista, key=lambda i: i[2]))

# Método usando função
def ordem(pos):
    return pos[1]
lista.sort(key=ordem)
print(lista)