from Embarcacion import Embarcacion
from Velero import Velero
from Lancha import Lancha
import csv

class GestorEmbarcacion:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEmbarcacion(self, embarcacion):
        self.__listaE.append(embarcacion)    

    def cargaEmbarcacion(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Rec Parcial 2 Tema 1 2025/embarcaciones.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')    
            next(reader)
            for fila in reader:
                nomE = fila[0]
                tipo = fila[1]
                eslora = fila[2]
                anioF = int(fila[3])
                costo = float(fila[4])
                dispo = fila[5].strip().lower() == 'true'    
                cantD = int(fila[6])
                if tipo == 'Velero':
                    cantV = int(fila[7]) 
                    embarcacion = Velero(cantV,nomE,eslora,anioF,costo,dispo,cantD)
                elif tipo == 'Lancha':
                    potencia = float(fila[8])
                    embarcacion = Lancha(potencia,nomE,eslora,anioF,costo,dispo,cantD)
                self.__listaE.append(embarcacion)                   

    def crearYagregarEmbar(self,embarcacion):
        i = 0
        encontrado = False
        if isinstance(embarcacion, Embarcacion):
            while i < len(self.__listaE) and not encontrado:
                if embarcacion.getNomE() == self.__listaE[i].getNomE():
                    encontrado = True
                else: 
                    i+=1
            if encontrado:
                raise ValueError
            else:
                self.__listaE.append(embarcacion)

    def alquilar(self,xnom):
        i = 0
        encontrado = False
        while i < len(self.__listaE) and not encontrado:
            if self.__listaE[i].getNomE() == xnom:
                encontrado = True
                if self.__listaE[i].getDispo():
                    self.__listaE[i].alquilar()
                    dias = int(input("Ingrese cantidad de dias a alquilar: "))
                    self.__listaE[i].setDias(dias)
                    print("Embarcacion Alquilada.")
                else:
                    print("Esta embarcacion ya fue alquilada.")
            else:
                i+=1
        if not encontrado:
            print("No se encontro la embarcacion.")                                                            

    """def mostrarAlquilado(self):
        for i in len(self.__listaE):
            if self.__listaE[i].alquilar() == 'True':
                self.__lista[i].mostrarAlquilado()"""

    def mostrarAlquilado(self):
        for i in len(self.__listaE): 
            if not self.__listaE[i].getDispo():
                self.__lista[i].mostrarAlquilado()   

    def mostrarDisponible(self):
        for i in len(self.__listaE):
            if self.__listaE[i].getDispo():
                print(f"""
                       Nombre: {self.__lista[i].getNomE()}
                       Costo: {self.__lista[i].getCosto()}
                       Tipo: {type(self.__lista[i].__name__)}
                       """)
                if type(self.__listaE[i]) == Velero:
                    print(f"Potencia: {self.__lista[i].getPotencia()}")  
                elif type(self.__listaE[i]) == Lancha:
                    print(f"Cantidad de Velas: {self.__listaE[i].getCantV()}")         