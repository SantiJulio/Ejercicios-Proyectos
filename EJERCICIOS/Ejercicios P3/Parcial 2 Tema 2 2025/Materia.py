from Tema import Tema

class Materia:
    __cod: str
    __nomM: str
    __desp: str
    __anio: int
    __listaT: list

    def __init__(self,cod,nomM,desp,anio):
        self.__cod = cod
        self.__nomM = nomM
        self.__desp = desp
        self.__anio = anio
        self.__listaT = []

    def getCod(self):
        return self.__cod

    def getNomM(self):
        return self.__nomM

    def getDesp(self):
        return self.__desp

    def getAnio(self):
        return self.__anio

    def getListaT(self):
        return self.__listaT

    def agregarTema(self,tema):
        self.__listaT.append(tema) 

    def __str__(self):
        return(f"""
                Cod: {self.__cod}
                NomM: {self.__nomM}
                Desp: {self.__desp}
                Anio: {self.__anio}
                """)       
    
    def mostrarTema(self,xcod):
        for i in range(len(self.__listaT)):
            if self.__listaT[i].getCodM() == xcod:
                print(f"""
                       CodM: {xcod}
                       NomM: {self.__listaT[i].getNomT()}
                       Desc: {self.__listaT[i].getDesc()}
                       """)        

    def mostrarPorTema(self,xnomT):
        i = 0
        encontrado = False
        while i < len(self.__listaT) and not encontrado:
            if self.__listaT[i].getNomT() == xnomT:
                encontrado = True
            else: 
                i += 1
        return encontrado                      