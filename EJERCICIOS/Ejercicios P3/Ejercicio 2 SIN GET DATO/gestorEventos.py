from lista import Lista
import csv
from evento import Evento
from invitado import Invitado


class GestorEventos:
    __lista: Lista

    def __init__(self):
        self.__lista = Lista()

    def cargar_eventos(self):
        archivo = open("eventos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregar_evento(fila[0], fila[1], fila[2], fila[3])

    def cargar_invitados(self):
        archivo = open("invitados.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregar_invitado(int(fila[0]), fila[1], fila[2], fila[3], fila[4])


    def agregar_evento(self, id, nombre, fecha, tipo):
        evento = Evento(id, nombre, fecha, tipo)
        self.__lista.agregar_evento(evento)

    def agregar_invitado(self, id_evento, nombre, dni, email, direccion):
        invitado = Invitado(nombre, dni, email, direccion)
        self.__lista.agregar_invitado(id_evento, invitado)

    def mostrar_eventos(self):
        for evento in self.__lista:
            print(evento)

    def mostrar_invitados_por_tipo(self, tipo):
        existe = False
        for evento in self.__lista:
            if evento.get_tipo() == tipo:
                existe = True
                evento.mostrar_invitados()

        if not existe:
            print(f"No hay eventos para el tipo {tipo}")


    def mostrar_eventos_por_invitado(self, dni):
        existe = False
        for evento in self.__lista:
            inv = evento.buscar_invitado_por_dni(dni)

            if inv != -1:
                existe = True
                print(evento.get_nombre())

        if not existe:
            print("No existe el invitado")

    
    def mostrar_conferencias(self, fecha):
        existe = False
        for evento in self.__lista:
            if evento.get_tipo() == "Conferencia" and evento.get_fecha() == fecha:
                existe = True
                print(evento)
        
        if not existe:
            print("No hay conferencias para esa fecha")
        
