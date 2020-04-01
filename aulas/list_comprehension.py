#LIST COMPREHENSION

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, v1) for v in l1 for v1 in range(2)]

l2 = ['Thiago', 'Maria', 'Suzana']
ex4 = [v.replace('a', '@') for v in l2]

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)

ex5 = [(x, y) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex7 = [v if v % 4 == 0 and v % 7 == 0 else 0 for v in l3]

#Exercicio
string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + 10] for i in range(0, len(string), 10)]

print(lista)
ponto = '.'.join(lista)
print(ponto)


