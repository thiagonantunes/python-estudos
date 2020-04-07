#REDUCE -> FUNCTOOLS  contador

from functools import  reduce

lista = [1,2,3,4,5,6,7,8,9,10]
soma_lista = reduce(lambda ac, i: ac + i, lista, 0)

print(soma_lista)

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

soma_valores = round(reduce(lambda ac, v: v['preço'] + ac, produtos, 0))
print(soma_valores / len(produtos))  #média

# identificar maior valor
lista = [12, 43, 3224, 123]
maior = reduce(lambda x,y: x if(x > y) else y, lista)