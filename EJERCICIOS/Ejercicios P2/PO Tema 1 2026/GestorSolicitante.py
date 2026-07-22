from Solicitante import Solicitante
import csv

class GestorSolicitante:
    lista: list

    def __init__(self):
        self.__lista = []

    def cargaSolicitante(self,solicitante):
        self.__lista.append(solicitante)   

    def leerSolicitante(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/PO Tema 1 2026/solicitante.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unSolicitante = Solicitante(int(fila[0]), fila[1], fila[2], int(fila[3]))   
                self.cargaSolicitante(unSolicitante)     
    
    def getLista(self):
        return self.__lista