print(chr(8594)) # imprime este símbolo →

#Enumerar uma lista, start indica o 1º valor
estacoes = ['Primvavera', 'Verão', 'Outono', 'Inverno']
tot = enumerate(estacoes, start=1)


courses = {'History', 'Math', 'Compsci', 'Physics'}
new_courses = {'Art', 'Math'}

#retorna valor comum nas duas lista
list1 = courses.intersection(new_courses)

#retorna a união das duas listas
list2 = courses.union(new_courses)

t1 = 1  # type: inteiro
t1 = 1, # type: lista

#DESEMPACOTAMENTO DE LISTAS
lista = ['Luiz', 'João', 'Maria',1,2,3,4,5,6,100]
n1, n2, *outra_lista, ultimo = lista
print(outra_lista[0])

#TROCANDO VALORES ENTRE VARIÁVEIS
x = 10
y = 'Luiz'
x, y = y, x 
print(f'x={x} e y={y}')



