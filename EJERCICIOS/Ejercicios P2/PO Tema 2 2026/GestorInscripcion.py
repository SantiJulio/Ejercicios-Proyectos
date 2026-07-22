from Inscripcion import Inscripcion
import csv
import numpy as np

class GestorInscripcion:
    arreglo: np.ndarray
    dimension: int
    cantidad: int
    incremento: int

    def __init__(self,dimension=5,incremento=5):
        self.__arreglo = np.empty(dimension, dtype=Inscripcion)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = incremento

    def cargaInscripcion(self,inscripcion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arreglo = np.resize(self.__arreglo, self.__dimension)
        self.__arreglo[self.__cantidad] = inscripcion
        self.__cantidad += 1

    def leerInscripcion(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/PO Tema 2 2026/inscripcionesCursos.csv', 'r') as archivo:           
            reader = csv.reader(archivo, delimiter=',')
            next(reader)
            for fila in reader:
                unaInscripcion = Inscripcion(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], int(fila[5]), int(fila[6]))
                self.cargaInscripcion(unaInscripcion)

    def mostrarInscMasUnCurso(self,dni):
        cont = 0
        for i in range(self.__cantidad):
            if self.__arreglo[i].getDniA() == dni:
                print(f"""
                   Identificador {self.__arreglo[i].getId()}
                   Descripcion {self.__arreglo[i].getDescripcion()}
                   """)
                cont +=1  

    def InscEnUnMismoCurso(self,xdni,xid,gestorAspirante):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__arreglo[i].getDniA() == xdni and self.__arreglo[i].getId() == xid:
                encontrado = True
            else: 
                i+=1                      
        if encontrado:
            cont = 0
            for j in range(self.__cantidad):
                if self.__arreglo[j].getDniA() == xdni and self.__arreglo[j].getId() == xid:
                    cont += 1        
            if cont > 1:        
                gestorAspirante.mostrarCosas(xdni)
                print(f"""
                       Descripcion {self.__arreglo[i].getDescripcion()}
                       Fecha {self.__arreglo[i].getFecha()}
                       """)
            else:
                print("Esta persona no esta repetida.")    