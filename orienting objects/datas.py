

class Datas:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def fomatada(self):
        print(f"A data é {self.__dia:02d}/{self.__mes:02d}/{self.__ano:02d}")
