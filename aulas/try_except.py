try:
    a = {'name':'Thiago'}
    print(a['name'])
    if a['name'] == 'Thiago':
        raise Exception
    var = 'old_var'
except KeyError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print('Código execuado com sucesso')
finally:  #será sempre executada
    print('Finalmente')

# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature

#     def drink_coffee(self):
#         if self.__temperature > 85:
#             #print('Coffee Too Hot')
#             raise Exception ('Coffee Too Hot')
#         elif self.__temperature < 65:
#             #print('Coffee Too Cold')
#             raise Exception ('Coffee Too Cold')
#         else:
#             print('Cofee Ok to Drink')

# cup = CoffeeCup(100)
# cup.drink_coffee()