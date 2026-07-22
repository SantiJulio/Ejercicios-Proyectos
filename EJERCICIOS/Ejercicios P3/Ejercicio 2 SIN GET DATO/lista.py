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

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        
        else:
            self.__indice += 1
            nodo = self.__actual
            self.__actual = self.__actual.get_siguiente()
            return nodo
        
    def agregar_evento(self, evento):
        nodo = Nodo(evento)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def agregar_invitado(self, id_evento, invitado):
        aux = self.__comienzo
        band = False

        while(aux is not None and not band):
            if aux.get_id() == id_evento:
                band = True
            else:
                aux = aux.get_siguiente()

        if aux is None:
            print("Evento no encontrado")
        else:
            aux.agregar_invitado(invitado)
