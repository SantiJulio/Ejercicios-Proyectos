from Colectivo import Colectivo
import csv
import numpy as np

class GestorColectivo:
    __ndarray: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int

    def __init__(self,dimension=5,incremento=5):
        self.__ndarray = np.empty(dimension, dtype = Colectivo)
        self.__incremento = incremento
        self.__cantidad = 0
        self.__dimension = dimension

    def cargaGestorColectivo(self,colectivo):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__ndarray = np.resize(self.__ndarray, self.__dimension)
        self.__ndarray[self.__cantidad] =  colectivo
        self.__cantidad += 1 
    
    def leerColectivo(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Empresa de Transporte/colectivos.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unColectivo = Colectivo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
                self.cargaGestorColectivo(unColectivo)
    
    def listadoTramos(self,gestorTramos,xdni):
        i=0
        encontrado=False
        patente = None
        while i < self.__cantidad and not encontrado:
            if self.__ndarray[i].getDniChofer() == xdni:
                encontrado = True
                patente = self.__ndarray[i].getPatente()
            else:
                i+=1
        print(i)            
        if encontrado:
            gestorTramos.mostrarDatosPorPatente(patente)
        else:
            print("No se encontro el dni")    

    def mostrarGastoTotal(self,gestorTramo):
        for i in range(self.__cantidad): 
            Colectivo = self.__ndarray[i]
            patente = Colectivo.getPatente()
            kmTotales = gestorTramo.totalKilometros(patente)  # Le pedimos al otro gestor los km de ESTA patente actual
            gasto = (kmTotales * Colectivo.getConsumo()) / 100 # Calculamos el gasto (usando la variable de clase de Colectivo)
            print(f"{patente:<10} {kmTotales:<10.2f} {gasto:<20.2f}") #Estetica al codigo --CULTURISMO--    