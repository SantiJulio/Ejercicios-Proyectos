from ClaseNodo import Nodo

class Lista:
    __cabeza: Nodo
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__tope = 0

    def getCabeza(self):
        return self.__cabeza

    def getTope(self):
        return self.__tope 

    def agregar(self,unComplejo):
        nodo = Nodo(unComplejo)
        nodo.setSiguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1 

    def buscarPlanta(self,xplanta):
        aux = self.__cabeza
        for aux in self.__cabeza:
            aux = self.buscarPlan(xplanta)
            aux = aux.getSiguiente()

    def buscarIdNroCant(self,xid,xnro,xcantDias):
        aux = self.__cabeza
        while aux is not None:
            if aux.getId() == xid:
                aux = aux.registrarAlq(xid,xnro,xcantDias)
            aux = aux.getSiguiente()

    def mostrarPorIngreso(self):
        aux = self.__cabeza
        for aux in self.__cabeza:
            acum = aux.mostrarTotal()
            aux = aux.getSiguiente()
        return acum 

    def calcularTotal(self,xid):
        aux = self.__cabeza
        while aux is not None:
            if aux.getId() == xid:
                aux = aux.calcularT(xid)
            aux = aux.getSiguiente() 

    def mostrarPos(self,pos):
        if pos < 0 or pos >= self.__tope:
            raise IndexError
        aux = self.__cabeza
        for _ in range(pos):
            aux = self.mostrarDatos()
            aux = aux.getSiguiente()                            