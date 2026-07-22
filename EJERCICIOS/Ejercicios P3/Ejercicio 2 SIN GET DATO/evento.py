from invitado import Invitado

class Evento:
    __id: int
    __nombre: str
    __fecha: str
    __tipo: str
    __invitados: list[Invitado]

    def __init__(self, id, nombre, fecha, tipo):
        self.__id = int(id)
        self.__nombre = nombre
        self.__fecha = fecha
        self.__tipo = tipo
        self.__invitados = []

    def __str__(self):
        invitados = ", ".join(str(inv) for inv in self.__invitados)
        return f"ID: {self.__id} - Nombre: {self.__nombre} - Invitados: {invitados}"

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_fecha(self):
        return self.__fecha
    
    def get_tipo(self):
        return self.__tipo
    
    def agregar_invitado(self, invitado):
        if isinstance(invitado, Invitado):
            self.__invitados.append(invitado)

    def mostrar_invitados(self):
        for inv in self.__invitados:
            print(inv)

    def buscar_invitado_por_dni(self, dni):
        i = 0
        
        while(i<len(self.__invitados) and self.__invitados[i].get_dni() != dni):
            i += 1

        if i == len(self.__invitados):
            inv = -1
        else:
            inv = i

        return inv