class Escritor():
    def __init__(self, nome):
        self.nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def digitar(self):
        print('Máquina está digitando...')

    def analisar(self):
        print('Máquina está analisando...')

escitor = Escritor('Angela Nunes')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escitor.nome)
print(caneta.marca)
Escritor.ferramenta = maquina  # Aqui é feita a associação
Escritor.ferramenta.analisar()
