

class Cliente:

    def __init__(self, __nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter #nesse caso o "nome" é o property transformado
    def nome(self, nome):
        self.__nome = nome