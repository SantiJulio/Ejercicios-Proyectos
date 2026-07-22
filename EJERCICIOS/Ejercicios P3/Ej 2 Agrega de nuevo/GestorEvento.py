from Evento import Evento
from Invitado import Invitado
import csv

class GestorEvento:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEvento(self,evento):
        if isinstance(evento,Evento):
            self.__listaE.append(evento)
        else:
            raise TypeError

    def cargaEvenInv(self):
        with open('D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Ej 2 Agrega de nuevo\eventos.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                unEvento = Evento(int(fila[0]),fila[1],fila[2],fila[3])
                self.agregarEvento(unEvento)

        with open('D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Ej 2 Agrega de nuevo\Invitados.csv', 'r') as archivoI:
            readerI = csv.reader(archivoI,delimiter=';')
            next(readerI)
            for fila in readerI:
                id = int(fila[0])
                nomI = fila[1]
                dni = int(fila[2])
                email = fila[3]
                dir = fila[4]
                for i in self.__listaE:
                    if i.getIdE() == id:
                        unInvitado = Invitado(id,nomI,dni,email,dir)
                        i.agregarInvitado(unInvitado)

    def agregarEv(self,idE,nomE,fecha,tipo): 
        i = 0
        encontrado = False
        while i < len(self.__listaE) and not encontrado:
            if self.__listaE[i].getIdE() == idE:
                encontrado = True
            else: 
                i += 1
        if encontrado:
            raise ValueError("Id de Evento ya cargado anteriormente.")
        else:
            self.agregarEvento(idE,nomE,fecha,tipo)

    def agregarIn(self,id,nomI,dni,email,dir):
        i = 0
        encontrado = False
        while i < len(self.__listaE) and not encontrado:
            if self.__listaE[i].getIdE() == id:
                encontrado = True
            else: 
                i += 1
        if encontrado:
            unInvi = Invitado(id,nomI,dni,email,dir)
            self.agregarInvitado(unInvi)

    def mostrarPorTipo(self,xtipo): 
        for i in range(len(self.__listaE)):
            if self.__listaE[i].Tipo() == xtipo:
                self.__listaE[i].mostrarInvi(self.__listaE[i].getIdE())            

    def mostrarPorDni(self,xdni):
        for i in range(len(self.__listaE)):
            if self.__listaE[i].mostrarRegistrado(xdni):
                print(f"Nombre del Evento: {self.__listaE[i].getNomE()}")
            else:
                print(f"No esta registrado en el evento {i}")        