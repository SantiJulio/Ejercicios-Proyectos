from Nodo import Nodo

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

    def agregar(self,unEquipo):
        nodo = Nodo(unEquipo)
        nodo.setSiguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1 

    def mostrarPos(self,pos):
        if pos < 0 or pos >= self.__tope:
            raise IndexError
        aux = self.__cabeza
        for _ in range(pos):
            aux = self.mostrarDatos()
            aux = aux.getSiguiente()
        return aux                                   