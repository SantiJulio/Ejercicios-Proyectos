from nodo import Nodo
class ListaInmuebles:
    __comienzo: Nodo
    __actual: Nodo

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def agregar(self, nuevoInm):
        nuevoNodo = Nodo(nuevoInm)

        if self.__comienzo is None:
            self.__comienzo = nuevoNodo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nuevoNodo)

    def __iter__(self):
        self.__actual = self.__comienzo
        return self

    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        else:
            inmueble = self.__actual.getInmueble()
            self.__actual = self.__actual.getSiguiente()
            return inmueble
