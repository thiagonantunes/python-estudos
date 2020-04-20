class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if self.ligado:
            return
        print(f'{self.nome} ligado')
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return
        print(f'{self.nome} foi desligado')
        self.ligado = False


class LogMixin:
    @staticmethod
    def write(msg):
        with open('/PythonCurso/ergo_project/log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


class Smartphone(Eletronico, LogMixin):  # <- Herança multipla aqui
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self.ligado:
            info = f'{self.nome} não está ligado' 
            print(info)
            self.log_error(info)
            return
        if self.conectado:
            error = f'{self.nome} já está conectado' 
            print(error)
            self.log_error(error)
            return
        info = f'{self.nome} está conectado' 
        print(info)
        self.log_info(info)
        self.conectado = True

    def desconectar(self):
        if not self.conectado:
            error = f'{self.nome} não está conectado' 
            print(error)
            self.log_error(error)
            return
        info = f'{self.nome} foi desligado'
        print(info)
        self.log_info(info)
        self.conectado = False

smart = Smartphone('Iphone')

smart.conectar()
smart.desligar()
smart.ligar()
smart.conectar()
smart.conectar()
smart.conectar()
smart.desligar()
smart.conectar()
smart.desconectar()