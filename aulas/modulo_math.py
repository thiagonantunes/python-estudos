import math

PI = math.pi

def dobra_valor(valor):
    return [x * 2 for x in lista]

def multiplica(valor):
    r = 1
    for i in valor:
        r *= i
    return r

if __name__ == '__main__':  #não será importado 
    lista = [1,2,3,4,5]
    print(PI)
    print(dobra_valor(lista))
    print(multiplica(lista))