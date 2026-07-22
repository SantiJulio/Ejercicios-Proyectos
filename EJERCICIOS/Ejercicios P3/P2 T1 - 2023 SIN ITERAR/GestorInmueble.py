from Inmueble import Inmueble
from Casa import Casa
from Departamento import Departamento
from ClaseLista import Lista
import csv

class Gestor:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarInmueble(self,unInmueble):
        if isinstance(unInmueble,Inmueble):
            self.__lista.agregar(unInmueble)
        else:
            raise TypeError    

    def cargaInmueble(self):
        archivo = open('inmuebles.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            tipo = fila[0]
            if tipo == 'C':
                unInmueble = Casa(fila[1],fila[2],float[3],float(fila[8]))
                self.agregarInmueble(unInmueble)
            elif tipo == 'D':
                unInmueble = Departamento(fila[1],fila[2],float[3],int(fila[4]),int(fila[5]),int(fila[6]),int(fila[7]))
                self.agregarInmueble(unInmueble)
        archivo.close()  
    
    def mostrarPorDormi(self,xcD): 
        for i in self.__lista:
            if isinstance(i,Departamento):
                if i.getCantD() <= xcD:
                    print(i)    
                    print(f"Importe de Venta: {i.importeVenta()}")

    def mostrarCasa(self):
        for i in self.__lista:
            if isinstance(i,Casa):
                print(f"""
                       Direccion: {i.getDirec()}
                       Superficie Cubierta: {i.getSupC()}
                       Importe de Venta: {i.importeVenta()}
                       """)                    