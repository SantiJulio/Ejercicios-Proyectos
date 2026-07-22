from Complejo import Complejo
from Cabaña import Cabaña
from ClaseLista import Lista
import csv

class Gestor:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarComplejo(self,unComplejo):
        if isinstance(unComplejo,Complejo):
            self.__lista.agregar(unComplejo)
        else:
            raise TypeError    

    def cargaComplejo(self):
        archivo = open('complejos.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            unComplejo = Complejo(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
            self.agregarComplejo(unComplejo)
            self.cargaCabaña(unComplejo)
        archivo.close()

    def cargaCabaña(self,unComplejo):
        archivo = open('cabañas.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            if unComplejo.getId() == fila[0]:
                nro = int(fila[1])
                planta = fila[2]
                cantD = int(fila[3])
                costo = float(fila[4])
                estado = fila[5]
                for i in self.__lista:
                    i.agregarCabaña(nro,planta,cantD,costo,estado)

    def mostrarPorPlanta(self,xplanta):
        self.__lista.buscarPlanta(xplanta)

    def mostrarPorIdNroCant(self,xid,xnro,xcantDias):
        self.__lista.buscarIdNroCant(xid,xnro,xcantDias) 

    def mostrarPorComplejo(self):
        for i in self.__lista:
            total = i.mostrarPorIngreso()
            print(f"Ingreso Total: {total}") 

    def calcularPorComplejo(self,xid):
        self.__lista.calcularTotal(xid)

    def mostrarPorPos(self,pos):
        self.__lista.mostrarPos(pos)        