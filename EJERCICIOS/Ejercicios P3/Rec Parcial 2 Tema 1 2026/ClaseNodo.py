from Complejo import Complejo

class Nodo:
    __complejo: Complejo
    __siguiente: object

    def __init__(self,complejo,siguiente):
        self.__complejo = complejo
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente  

    def getId(self):
        return self.__complejo.getId() 

    def buscarPlan(self,xplanta):
        self.__complejo.buscarP(xplanta)         

    def registrarAlq(self,xid,xnro,xcantDias):  
        self.__complejo.registrar(xid,xnro,xcantDias)  

    def mostrarTotal(self):
        return self.__complejo.mostrarIngTotal()

    def calcularT(self,xid):
        self.__complejo.calcular(xid) 

    def mostrarDatos(self):
        self.__complejo.mostrar()       