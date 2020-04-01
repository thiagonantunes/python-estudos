#OPERADOR TERNÁRIO

logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'

# Expressão acima equivale a expressão abaixo
if logged_user:
    msg1 = 'Usuário logado'
else:
    msg1 = 'Usuário precisa logar'
print(msg, msg1)

# outro exemplo
idade = input('Idade: ')

if not idade.isnumeric(): # validação para receber apenas número
    print('Apenas números')
else:
    maior = (int(idade) >= 18)
    msg = 'pode acessar' if maior else 'Proibido para menores'
    print(msg)
