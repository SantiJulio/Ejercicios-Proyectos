from Evento import Evento
from Invitado import Invitado
import csv

class GestorEvento:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEvento(self,unEvento):
        self.__listaE.append(unEvento)

    def cargaEvento(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/EJ 2 Agregacion/eventos.csv','r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unEvento = Evento(int(fila[0]),fila[1],fila[2],fila[3])
                self.agregarEvento(unEvento)        
        
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/EJ 2 Agregacion/invitados.csv','r') as archivoC:
            readerC = csv.reader(archivoC, delimiter=';')
            next(readerC)
            for fila in readerC:
                    idE = int(fila[0])
                    nombreI = fila[1]
                    dni = int(fila[2])
                    email = fila[3]
                    direccion = fila[4]
                    for evento in self.__listaE:
                        if evento.getId() == idE:
                            unInvitado = Invitado(idE,nombreI,dni,email,direccion)
                            evento.agregarInvitado(unInvitado)    

    def agregarInvitadoEvento(self,xid,xn,xdni,xe,xdir):
        i = 0
        encontrado = False
        while i < len(self.__listaE) and not encontrado:
            if self.__listaE[i].getId() == xid:
                unInvitado = Invitado(xid,xn,xdni,xe,xdir)
                self.__listaE[i].agregarInvitado(unInvitado)
                print(f"Invitado agregado correctamente.")
                encontrado = True
            else:
                i+=1

    def mostrarNombreInvitado(self,xtipo):
        for evento in self.__listaE:
            if evento.getTipo() == xtipo:
                print(f"\nEvento: {evento.getNombreE()}")
                print("Invitados:")
                for invitado in evento.getListaI():
                    print(invitado.getNombreI())

    def mostrarRegistrado(self,xdni): 
        i = 0
        encontrado = False
        while i < len(self.__listaE):                         
            evento = self.__listaE[i]
            for invitado in evento.getListaI():
                if invitado.getDni() == xdni:
                    encontrado = True
                    print(f"Nombre del Evento en el que el invitado {xdni} esta registrado es: {evento.getNombreE()}.")
            i+=1        
        if not encontrado:
            print("El invitado {xdni} no esta registrado en ningun evento.") 

    def mostrarPorFecha(self,xfecha):
        encontrado = False
        for evento in self.__listaE:
            if evento.getFecha() == xfecha and evento.getTipo() == 'Conferencia':
                print(f"Nombre del evento: {evento.getNombreE()}")
                encontrado = True
        if not encontrado: 
            print("No se encontro un evento para esa fecha.")