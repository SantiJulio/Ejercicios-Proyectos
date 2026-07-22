from Drones import Dron
import csv
import numpy as np

class gestorDron:
    __drones : np.ndarray
    __cantidad : int
    __dimension : int
    __incremento : int

    def __init__ (self,dimension = 5,incremento = 5):
        self.__drones = np.empty(dimension, dtype=Dron)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def cargaDrones(self,unDron):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__drones.resize(self.__dimension)
        self.__drones[self.__cantidad] = unDron
        self.__cantidad += 1

    def leerDrones(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Ejercicio IA/drones.csv','r') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                dron = Dron(fila[0],fila[1],fila[2],int(fila[3]),fila[4])
                self.cargaDrones(dron)

    def listarEinformar(self,xdni,gestorEnvios):  
        i = 0
        encontrado = False
        referencia = None
        while i < self.__cantidad and not encontrado:
            if self.__drones[i].getDniO() == xdni:
                encontrado = True
                referencia = self.__drones[i]
            else:
                i+=1
        if encontrado:
            acumulador = 0
            for j in range(len(gestorEnvios.getLista())):
                if gestorEnvios.getLista()[j].getIdDr() == referencia.getIdDron():
                    print(f"""
                            Barrio Origen:{gestorEnvios.getLista()[j].getBarrioOr()}
                            Barrio Destino:{gestorEnvios.getLista()[j].getBarrioDes()}
                            Tiempo de vuelo:{gestorEnvios.getLista()[j].getTiempo()}
                            """)
                    if acumulador < gestorEnvios.getLista()[j].getTiempo():
                        acumulador += gestorEnvios.getLista()[j].getTiempo() 
            print(f"La distancia total del dron {referencia.getIdDron()} es de {acumulador}")                   
        else:
            print("No se encontro el dni") 
                               
    def mostrarTiempoGasto(self,gestorEnvios):
        for i in range(self.__cantidad):
            dron = self.__drones[i]
            idD = dron.getIdDron()
            totalVuelo = gestorEnvios.totalTiempo(idD)
            gasto = (totalVuelo * dron.getConsumo()) / 100
            print(f"{idD:<10} {totalVuelo:<10.2f} {gasto:<20.2f}")              