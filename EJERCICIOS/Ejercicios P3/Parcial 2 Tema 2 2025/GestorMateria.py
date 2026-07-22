from Materia import Materia
from Tema import Tema
import csv

class GestorMateria:
    __listaM: list

    def __init__(self):
        self.__listaM = []

    def agregarMateria(self,materia):
        if isinstance(materia,Materia):
            self.__listaM.append(materia)
        else:
            raise TypeError    

    def cargaMatYTema(self):
        with open(r'D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Parcial 2 Tema 2 2025\materias.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                unaMateria = Materia(fila[0],fila[1],fila[2],int(fila[3]))
                self.agregarMateria(unaMateria)    

        with open(r'D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\Parcial 2 Tema 2 2025\temas.csv', 'r') as archivoT:
            readerT = csv.reader(archivoT,delimiter=',')
            next(readerT)
            for fila in readerT:
                codM = fila[0]
                nomT = fila[1]
                desc = fila[2]
                for i in len(self.__listaM):
                    if self.__listaM[i].getCod() == codM:
                        unTema = Tema(codM,nomT,desc)
                        self.agregarTema(unTema)

    def agregarMat(self,cod,nomM,desp,anio):
        i = 0
        while i < len(self.__listaM):
            if self.__listaM[i].getCod() == cod:
                raise ValueError
            else:
                unaMateria = Materia(cod,nomM,desp,anio)  
                self.listaM[i].agregarMateria(unaMateria)             
            i += 1 

    def agregarTema(self,codM,nomT,desc):
        i = 0
        encontrado = False
        while i < len(self.__listaM) and not encontrado:
            if isinstance(self.__listaM[i],Materia):
                if self.__listaM[i].getCod == codM:
                    encontrado = True
                else:  
                    i += 1
            else:
                raise TypeError        
        if encontrado:
            unTema = Tema(codM,nomT,desc)
            self.__listaM[i].agregarTema(unTema)

    def listarMatAnuales(self,xanio):
        for i in range(len(self.__listaM)):
            if self.__listaM[i].getAnio() == xanio and self.__listaM[i].getDesp() == "Anual":
                self.__listaM[i].mostrarTema(self.__listaM[i].getCod())
                print(f"Nombre de la materia: {self.__listaM[i].getNomM}")   
    
    def mostrar(self,xnomT):
        i = 0
        encontrado = False
        while i < len(self.__listaM) and not encontrado:
            if self.__listaM[i].mostrarPorTema(xnomT):
                encontrado = True
            else:
                i += 1
        if encontrado:
           print(f"""
                   Nombre Materia: {self.__listaM[i].getNomM()}
                   Anio de dictado: {self.__listaM[i].getAnio()}
                   """)              