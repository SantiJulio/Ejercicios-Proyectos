from EventoC import EventoC

class Congreso(EventoC):
    __cantConf: int
    __listaD: list

    def __init__(self,cantConf,cod,tit,inst,fecha,cant):
        super().__init__(cod,tit,inst,fecha,cant)
        self.__cantConf = cantConf
        self.__listaD = []

    def getCantConf(self):
        return self.__cantConf

    def getListaD(self):
        return self.__listaD   

    def agregarDisertante(self, unDisertante):
        self.__listaD.append(unDisertante)     