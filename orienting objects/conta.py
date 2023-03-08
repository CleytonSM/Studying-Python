

class Conta:

    def __init__(self, numero, saldo, titular, limite):
        print("Armazenando objeto ...{}".format(self))
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.__limite = limite

    def extrato(self):
        print("O titular {}, possui o saldo de R$ {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor R$ {} inserido ultrapassou o seu limite.".format(valor))
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def conta(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
