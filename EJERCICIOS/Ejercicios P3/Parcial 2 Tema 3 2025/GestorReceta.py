from Receta import Receta
import csv

class GestorReceta:
    __listaR: list
    
    def __init__(self):
        self.__listaR = []

    def agregarReceta(self,receta):
        if isinstance(receta,Receta):
            self.__listaR.append(receta)
        else:
            raise TypeError

    def cargaRecIng(self):
        with open(r'D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Parcial 2 Tema 3 2025\recetas.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                unaReceta = Receta(int(fila[0]),fila[1],fila[2])
                self.agregarReceta(unaReceta)

        with open(r'D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Parcial 2 Tema 3 2025\ingredietes.csv', 'r') as archivoI:
            readerI = csv.reader(archivoI,delimiter=',')
            next(readerI)
            for fila in readerI:
                id = int(fila[0])
                nomI = fila[1]
                unidad = fila[2]
                stock = int(fila[3])
                for i in range(len(self.__listaR)):
                    if self.__listaR[i].getIdR() == id:
                        self.__listaR[i].agregarIngrediente(id,nomI,unidad,stock)    

    def agregarIng(self,id,nomI,unidad,stock):
        i = 0
        encontrado = False
        while i < len(self.__listaR) and not encontrado:
            if self.__listaR[i].getIdR() == id:
                encontrado = True
            else: 
                i += 1
        if encontrado: 
            self.__listaR[i].agregarIngrediente(id,nomI,unidad,stock)                               

    def mostrarIng(self,xnomR,pos):
        i = 0
        encontrado = False
        while i < len(self.__listaR) and not encontrado:
            if self.__listaR[i].NomR() == xnomR and pos >= 0 or pos <= len(self.__listaR):
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError("No existe un ingrediente en esa posicion. Intente con otra.")
        else:
            print(self.__listaR[pos])

    def mostrarRec(self,xnomI):
        for i in range(len(self.__listaR)):
            if self.__listaR[i].mostrarPorNom(xnomI):
                print(f"Nombre Receta: {self.__listaR[i].getNomR()}")