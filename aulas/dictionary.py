"""
DICIONÁRIO
"""

d1 = {'chave1':'item 1', 'chave2': 'item2'}
d2 = dict(chave1='item 1', chave2 ='item 2')  #outra maneira de criar dicionário
d2['nova_chave'] = 'novo item'  # adicionando novo item no dicionário
d1['chave'] = 'item'

#para saber se uma key está no dicionário, caso não exista a chave, imprimi valor None
print(d1.get('chave', 'Not found'))

#outra maneira de mostrar o valor
print (d2['chave2']) 
print(d2)

# dicionário aceita string, int e tuple como chave
d3 ={'str': 'valor', 123: 'segundo valor', (1,2): 'terceiro valor'}

#deletar chave
del d3[123]

print('segundo valor' in d3.values())

print(d3)
clientes = {'cliente1':{'nome': 'Thiago', 'sobrenome': 'Antunes'}, 'cliente2':{'nome': 'Simone','sobrenome': 'Rodrigues'}}

# for clientes_k, clientes_v in clientes.items():
#   print (clientes_k)
#   for dados_k, dados_v in clientes_v.items():
#     print(f'\t{dados_k}: {dados_v}')


students = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
students.update({'phone': '5633-5000', 'name': 'Mary'})
print(students.get('phone', 'not found'))
del students['phone']
print(students)
age = students.pop('age')
print(students)
print(age)



"""
DICITONARY COMPREHENSION
"""

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor 2')
]
d1 = {x: y for x, y in lista}
d2 = {f'Chave: {x}': x*3 for x in range(3,8)}
# print(d1, d2)