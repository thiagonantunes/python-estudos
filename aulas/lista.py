'''
Listas em Python
fatiamento, append, insert, pop, del, clear, extend, +, min, max, range
'''

str = 'o rato roeu a roupa do rei de roma'
nova_frase = ''
for letra in str:
    if letra in 'r':
        nova_frase += letra.upper()
    elif letra in 'a':
        nova_frase = nova_frase + '@'
    else:
        nova_frase += letra
print(nova_frase)

lista = ['A', 'B', 'C', 'D', 'E', 10.5] 

# alterar conteúdo do item 5
lista[5] = 'Qualquer outra coisa'

lista1 = [1,2,3]
lista2 = [3,4,5]
lista3 = lista1 + lista2  #concatenar
print(lista3)
lista1.insert(0, 'banana')  #insere item na posição informada
lista1.pop()  #exclui o último item da lista
lista1.extend(lista2)
print(lista1)
print(lista2)
del(lista1[0])  #exclui o item escolhido
print(lista1)

lista = list(range(0,11))  #comando lista -> cria uma lista dos valores de range
print(lista)

item = ['String', True, 10, -10.5]
for elem in item:
 print(f'O tipo de {elem} é {type(elem)}')

lista = ['Luiz Oátvio', 'Thiago', 'Maria']
for var in lista:
    if var.lower().startswith('t'):
        print(f'{var} começa com T')
        break  # colocar break para sair do laço, senão vai imprimir o else
    else:
        print('Nenhum nome começa com T')


#Exercício utilizando fatiamento
# secreta = 'perfume'
# digitadas = []
# cont = 3
# while True:
#     if cont < 1:
#         break
#     letra = input('Type a letter: ')
#     if len(letra) > 1:
#         print('Type only 1 letter.')
#         continue
#     if letra in secreta or letra not in digitadas:
#         digitadas.append(letra)
#     if letra in secreta:
#         print(f'A letra "{letra}" tem na palavra secreta')
#     else:
#         print(f'A letra "{letra}" não tem na palavra secreta')
#         digitadas.pop()
#         cont -= 1
#     while cont > 0: 
#         print(f'Você tem mais {cont} tentativas')
#         break
#     else:
#         print(f'Você perdeu, acabaram suas tentativas, a palavra era {secreta.upper()}')
#         break
#     secreto_temp = ''
#     for letra_secreta in secreta:
#         if letra_secreta in digitadas:
#             secreto_temp += letra_secreta
#         else:
#             secreto_temp += '*'
#     if secreto_temp == secreta:
#         print(f'PARABÉNS, você acertou, a palvra secreta é {secreta.upper()}')
#         break
#     else:
#         print(f'A palavra secreta está assim: {secreto_temp}')
