from EventoC import EventoC
from Congreso import Congreso
from Seminario import Seminario
from Taller import Taller
import csv

class GestorEventoC:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEvento(self,unEvento):
        self.__listaE.append(unEvento)

    def cargaEvento(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Ej 6 Herencia Simple, Poli y lista/eventos.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')        
            next(reader)
            for fila in reader:
                tipo = fila[0]
                cod = fila[1]   
                tit = fila[2]
                inst = fila[3]
                fecha = fila[4]
                cantMA = int(fila[5]) 
                if tipo == 'Congreso':
                    cantC = int(fila[6])  
                    evento = Congreso(cantC,cod,tit,inst,fecha,cantMA)
                elif tipo == 'Seminario':
                    tem = fila[7]
                    dur = fila[8]
                    res = fila[9]
                    evento = Seminario(tem,dur,res,cod,tit,inst,fecha,cantMA)
                elif tipo == 'Taller':
                    cantA = int(fila[10])
                    nomC = fila[11] 
                    evento = Taller(cantA,nomC,cod,tit,inst,fecha,cantMA)
                self.agregarEvento(evento) 
