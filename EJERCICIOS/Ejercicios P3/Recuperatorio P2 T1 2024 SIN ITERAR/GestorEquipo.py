from Equipo import Equipo
from Herramienta import Herramienta
from Maquinaria import Maquinaria
from ClaseLista import Lista
import csv

class GestorEquipo:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarEquipo(self,unEquipo):
        if isinstance(unEquipo,Equipo):
            self.__lista.agregar(unEquipo)
        else:
            raise TypeError    

    def cargaEquipo(self):
        archivo = open('equipos.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            tipo = fila[0]            
            if tipo == 'M':
                unEquipo = Maquinaria(fila[1],fila[2],int(fila[3]),fila[4],int(fila[5]),int(fila[6]),float(fila[7]),int(fila[8]),fila[9],int(fila[10]))
                self.agregarEquipo(unEquipo)
            elif tipo == 'E':
                unEquipo = Herramienta(fila[1],fila[2],int(fila[3]),fila[4],int(fila[5]),int(fila[6]),float(fila[7]),int(fila[8]),fila[11])
                self.agregarEquipo(unEquipo)
        archivo.close()    
        
    def mostrarPorPos(self,pos):
        tipo = self.__lista.mostrarPos(pos) 
        if isinstance(tipo,Maquinaria):
            print("Es una Maquinaria.")
        elif isinstance(tipo,Herramienta):
            print("Es una Herramienta.")                           

    def mostrarPorAnio(self,xa):
        cont = 0
        for i in self.__lista:
            if isinstance(i,Herramienta):
                if i.getAnioF() == xa:
                    cont += 1
        if cont > 0:
            print(f"Ese anio fueron fabricadas {cont} herramientas.")
        else:
            print("No se fabricaron herramientas ese anio.") 

    def mostrarPorCapac(self,xcapac):
        cont = 0
        for i in self.__lista:
            if isinstance(i,Maquinaria):
                if i.getCapac() <= xcapac:
                    cont += 1
        if cont > 0:
            print(f"Hay {cont} equipos de maquinaria pesada.")                                                   

    def mostrarTodo(self):
        for i in self.__lista:
            print(f"""
                Marca: {i.getMarca()} 
                Modelo: {i.getModelo()}
                Anio: {i.getAnioF()}
                TipoC: {i.getTipoC()}
                Potencia: {i.getPotencia()}
                Capac: {i.getCapac()}
                Tarifa: {i.tarifaAlquiler()}
                """)            