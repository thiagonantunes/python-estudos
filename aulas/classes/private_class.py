# ENCAPSULAMENTO
# PUBLIC, _PROTECTED, __PRIVATE
"""
utiliza _ para deixar o atributo protegido (pode ser alterado)
utiliza __ para deixar o atributo privado (não pode ser alterado)
"""
class DataBase():
    def __init__ (self):
        self.__dados = {}  # private

    @property
    def dados(self):
        return self.__dados

    def insert_client(self, id, nome):
        if 'clientes'not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
        
    def list_clients(self):
        for index, name in self.__dados['clientes'].items():
            print(index, name)

    def del_client(self, id):
        del self.__dados ['clientes'][id]

bd = DataBase()

bd.insert_client(1, 'Otávio')
bd.insert_client(2, 'Thiago')
bd.insert_client(3, 'Simone')
bd.del_client(3)
bd.list_clients()

print(bd.dados)
