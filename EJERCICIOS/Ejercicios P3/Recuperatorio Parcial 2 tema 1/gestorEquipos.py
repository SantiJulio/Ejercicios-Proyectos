from equipos import Equipo
from maquinaria import Maquinaria
from herramienta import Herramienta
from lista import Lista
import csv

class Gestor:
    __lista: Lista
    def __init__(self):
        self.__lista = Lista()

    def agregarEquipo(self, equipo):
        if isinstance(equipo, Equipo):
            self.__lista.agregar(equipo)
        else:
            raise TypeError("Debe ser un objeto Equipo")
    
    def cargar(self):
        archivo = open("equipos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            if fila[0] == "M":
                equipo = Maquinaria(fila[1], fila[2], int(fila[3]),fila[4],fila[5],int(fila[6]),float(fila[7]),int(fila[8]),fila[9],fila[10])
                self.agregarEquipo(equipo)
            elif fila[0] == "H":
                equipo = Herramienta(fila[1], fila[2], int(fila[3]),fila[4],fila[5],int(fila[6]),float(fila[7]),int(fila[8]),fila[9])
                self.agregarEquipo(equipo)
        archivo.close()

    def obtenerPorPosicion(self, posicion):
        equipo = self.__lista.obtener(posicion)

        if isinstance(equipo, Maquinaria):
            print("Es un equipo de tipo Maquinaria.")
        elif isinstance(equipo, Herramienta):
            print("Es un equipo de tipo Herramienta.")
    
    def contarHerramientaElectrica(self, anio):
        contador = 0

        for equipo in self.__lista:
            if isinstance(equipo, Herramienta):
                if equipo.getAnioFab() == anio:
                    contador += 1
        
        if contador == 0:
            print("No existen herramientas electricas con ese año.")
        else:
            print("Las maquinarias de ese año son: ", contador)
        
    def mostrarMaquinariaPesadaMenorIgual(self, capCarga):
        contar = 0
        for equipo in self.__lista:
            if isinstance(equipo, Maquinaria):
                if equipo.getCapCarga() <= capCarga:
                    contar += 1
        if contar == 0:
            print("No existen maquinarias pesadas con capacidad de carga menor o igual a la ingresada.")
        else:
            print("Las cantidad de maquinarias pesadas con capacidad menor o igual a la ingresada es de: ", contar)

    def mostrarTodosLosEquipos(self):
        for equipo in self.__lista:
            print(equipo)
            print(f"Tarifa final: ${equipo.calcularTarifa():.2f}")