from Excursiones import Excursion
from ClaseNodo import Nodo
from ExcursionesNauticas import ExcursionNautica
from ExcursionesTerrestres import ExcursionTerrestre
import csv

"""class ClaseLista:
    __excursiones : list

    def __init__(self):
        self.__excursiones = []

    def agregarExcursion(self, excursion):
        self.__excursiones.append(excursion)

    def leerExcursiones(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Ej 4 Herencia Simple y Polimorfismo/excursiones.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            next(reader)
            for fila in reader:              
                tipo = fila[0]
                nom = fila[1]
                des = fila[2]
                pre = float(fila[3])              
                if tipo == 'Terrestre':
                    km = float(fila[4])
                    alm = fila[5].strip().lower() == 'true'
                    excursion = ExcursionTerrestre(km, alm, nom, des, pre)                    
                elif tipo == 'Nautica':
                    dur = fila[6]
                    cMax = int(fila[7])
                    excursion = ExcursionNautica(dur, cMax, nom, des, pre)
                self.agregarExcursion(excursion)"""
            
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
        self.__actual = self.__comienzo
        self.__indice = 0
        return self 

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            excursion = self.__actual.getExcursion()
            self.__actual = self.__actual.getSiguiente()
            return excursion
    
           

    def crearYAgregarExcursion(self, tipo, nom, des, pre, km, alm, dur, cMax):
        if tipo == 'Terrestre':
            excursion = ExcursionTerrestre(km, alm, nom, des, pre)
        elif tipo == 'Nautica':
            excursion = ExcursionNautica(dur, cMax, nom, des, pre)
        self.agregarExcursion(excursion)

    def mostrarCantidad(self):
        cantET = 0
        cantEN = 0
        for i in self.__excursiones:
            if isinstance(i, ExcursionTerrestre):
                cantET += 1
            elif isinstance(i, ExcursionNautica):
                cantEN += 1
        print(f"Cantidad de excursiones terrestres: {cantET}") 
        print(f"Cantidad de excursiones nauticas: {cantEN}")               

    def mostrarNomDesPreF(self):
        for i in self.__excursiones:
            print(f"""
                  Nombre de la Excursion: {i.getNomExcursion()}
                  Destino {i.getDestino()}
                  Importe final a pagar {i.calcularPrecio()}
                   """)   