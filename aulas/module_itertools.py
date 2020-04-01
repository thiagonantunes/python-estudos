"""
COMBINATIONS, PERMUTATIONS, PRODUCT, GROUPBY, COUNT
"""

#COMBINATION, PERMUTATION E PRODUCT -> ITERTOOLS
#COMBINAÇÃO -> ORDEM NÃO IMPORTA
#PERMUTAÇÃO -> ORDEM IMPORTA
#PRODUTO -> ORDEM IMPORTA E REPETE VALORES ÚNICOS

from itertools import combinations, permutations, product

pessoas = ['Thiago', 'Simone', 'Otto', 'Luiz']
num = [1,2,3,4,5]

for grupo in product(pessoas, repeat=2):
    print(grupo)

for listas in combinations(num, 3):
    print(listas)

for listas in permutations(pessoas, 2):
    print(listas)


bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)

print(set(makes_100))

#GROUPBY -> ITERTOOLS
from itertools import groupby, tee  #tee -> faz cópia do iterador

alunos = [
    {'nome':'Luiz', 'nota':'A'},
    {'nome':'Thiago', 'nota':'B'},
    {'nome':'Otto', 'nota':'A'},
    {'nome':'Simone', 'nota':'C'},
    {'nome':'Leo', 'nota':'D'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)

# print(alunos)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  #fez duas cópias do valores_agrupados
    print(f'Agrupamento: {agrupamento}')
    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    for aluno in va1:
        print(f'--> {aluno["nome"]}')
    print()

#COUNT - ITERTOOLS
from itertools import count

#contador = count(start=5, step=0.1)

contador = count()
nomes = ['Thiago', 'Simone', 'Otto', 'Pablo', 'Ricardo']
geral = zip(contador, nomes)
print(list(geral))

print(next(contador))  #imprimi o próximo valor da lista
print(next(contador))

for valor in contador:
    print(round(valor, 2))  # função round arredonda valor
    if valor >= 10:
        break