from evento import Evento

class Nodo:
    __evento: Evento
    __siguiente: object

    def __init__(self, evento):
        self.__evento = evento
        self.__siguiente = None

    def __str__(self):
        return str(self.__evento)

    def get_siguiente(self):
        return self.__siguiente
    
    def set_siguiente(self, nodo):
        self.__siguiente = nodo


    def get_id(self):
        return self.__evento.get_id()

    def get_nombre(self):
        return self.__evento.get_nombre()
    
    def get_fecha(self):
        return self.__evento.get_fecha()

    def get_tipo(self):
        return self.__evento.get_tipo()


    def agregar_invitado(self, invitado):
        self.__evento.agregar_invitado(invitado)

    def mostrar_invitados(self):
        self.__evento.mostrar_invitados()

    def buscar_invitado_por_dni(self, dni):
        return self.__evento.buscar_invitado_por_dni(dni)
    