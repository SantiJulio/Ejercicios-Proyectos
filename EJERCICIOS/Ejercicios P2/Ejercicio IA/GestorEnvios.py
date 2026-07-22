from Envios import Envio
import csv

class gestorEnvio:
    __envios : list

    def __init__(self):
        self.__envios = []

    def cargarEnvios(self,unEnvio):
        self.__envios.append(unEnvio)

    def leerEnvios(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Ejercicio IA/envios.csv','r') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                envios = Envio(fila[0],fila[1],int(fila[2]),fila[3])
                self.cargarEnvios(envios)

    def getLista(self):
        return self.__envios
    
    def totalTiempo(self, idc):
        acumulador = 0
        for i in self.__envios:
            if i.getIdDr() == idc:
                acumulador += i.getTiempo()
        return acumulador
    
    def listarEnvios(self,xtiempo):     
        for i in range(len(self.__envios)):
            if self.__envios[i].getTiempo() > xtiempo:
                print(f"""
                       Barrio Origen {self.__envios[i].getBarrioOr()}
                       Barrio Destino {self.__envios[i].getBarrioDes()}
                       ID del Dron {self.__envios[i].getIdDr()}
                       """)         