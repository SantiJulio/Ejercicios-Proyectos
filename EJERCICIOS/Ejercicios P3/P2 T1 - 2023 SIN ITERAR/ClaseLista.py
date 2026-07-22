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

    def agregar(self,unInmueble):
        nodo = Nodo(unInmueble)
        nodo.setSiguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1    