

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

    def saca(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    def get_conta(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite