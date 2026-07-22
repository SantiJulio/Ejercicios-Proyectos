from nodo import Nodo

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def agregar(self, objeto):
        nodo = Nodo(objeto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def mostrar(self):
        aux = self.__comienzo

        while aux is not None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        self.__indice += 1
        nodo = self.__actual
        self.__actual = self.__actual.getSiguiente()
        return nodo.getDato()
    
    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.__tope:
            raise IndexError
        aux = self.__comienzo
        for _ in range(posicion):
            aux = aux.getSiguiente()
        return aux.getDato()
    
    ''' ---POR SI PIDEN ELIMINAR---
    def eliminarPorMarca(self, marca):
        aux = self.__comienzo
        anterior = None
        encontrado = False

        while aux is not None and not encontrado:
            if aux.getDato().getMarca() == marca:
                encontrado = True
            else:
                anterior = aux
                aux = aux.getSiguiente()

        if encontrado:
            if anterior is None:
                self.__comienzo = aux.getSiguiente()
            else:
                anterior.setSiguiente(aux.getSiguiente())
            self.__tope -= 1'''
    
    ''' ---ELIMINAR POR POSICION---
    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.__tope:
            raise IndexError

        aux = self.__comienzo
        anterior = None
        i = 0

        while i < posicion:
            anterior = aux
            aux = aux.getSiguiente()
            i += 1

        if anterior is None:
            self.__comienzo = aux.getSiguiente()
        else:
            anterior.setSiguiente(aux.getSiguiente())

        self.__tope -= 1'''