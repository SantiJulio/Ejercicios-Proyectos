from EventoC import EventoC

class Taller(EventoC):
    __cantA: int
    __nomC: str
    __listaM: list

    def __init__(self,cantA,nomC,cod,tit,inst,fecha,cant):
        super().__init__(cod,tit,inst,fecha,cant)
        self.__cantA = cantA
        self.__nomC = nomC
        self.__listaM = []

    def getCantA(self):
        return self.__cantA
    
    def getNomC(self):
        return self.__nomC
    
    def getListaM(self):
        return self.__listaM
    
    def getMateriales(self, unMaterial):
        return self.__listaM.append(unMaterial)