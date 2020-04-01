# ZIP - UNINDO ITERÁVEIS
# ZIP_LONGEST - ITERTOOLS

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Porto Alegre', 'Angra']
estados = ['SP', 'MG', 'BA']

#cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')

cidades_estados = zip(indice, cidades, estados)

# print(next(cidades_estados))
# print(list(cidades_estados))
# for valor in cidades_estados:
# print(valor)


for indice, cidades, estados in cidades_estados:
    print(indice, cidades, estados)

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,5]
soma = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=10)]  #soma todos elementos
soma1 = [x + y for x, y in zip(lista1, lista2)]  #soma a lista menor
print(soma)
print(soma1)

# 1º método
# soma = []
# for i in range(len(lista2)):
#    soma.append(lista1[i] + lista2[i])
# print(soma)

# 2º método
# for i, _ in enumerate(lista2):
#     soma.append(lista1[i] + lista2[i])
# print(soma)