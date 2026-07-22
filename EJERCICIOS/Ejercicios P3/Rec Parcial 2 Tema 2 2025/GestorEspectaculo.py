from Espectaculo import Espectaculo
from Concierto import Concierto
from Obra import Obra
import csv

class GestorEspectaculo:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEspectaculo(self,espectaculo):
        self.__listaE.append(espectaculo)   

    def cargaEspectaculo(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Rec Parcial 2 Tema 2 2025/espectaculos.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')    
            next(reader)   
            for fila in reader:
                nom = fila[0]
                fecha = fila[1]
                precio = float(fila[2]) 
                tipo = fila[3]
                if tipo == 'ObraTeatro':
                    nomD = fila[4]
                    dur = int(fila[5])
                    espectaculo = Obra(nomD,dur,nom,fecha,precio)
                elif tipo == 'Concierto':
                    banOart = fila[6]
                    cantM = int(fila[7])
                    espectaculo = Concierto(banOart,cantM,nom,fecha,precio)
                self.agregarEspectaculo(espectaculo) 

    def crearYagregarEspec(self,espectaculo):
        i = 0
        encontrado = False
        if isinstance(espectaculo, Espectaculo):
            while i < len(self.__listaE) and not encontrado: 
                if espectaculo.getFecha() == self.__listaE[i].getFecha():
                    encontrado = True
                else:
                    i+=1
            if encontrado:
                raise ValueError 
            else:
                self.agregarEspectaculo(espectaculo)
                print("Se agrego el espectaculo.")     

    def mostrarTodos(self):
        for i in len(self.__listaE):
            self.__lista[i].mostrarDatos()

    def listarSuperior(self):
        for i in len(self.__listaE):
            if self.__listaE[i].precioEntrada() > 10000:
                print(f"Nombre: {self.__lista[i].getNombre()}")

    def mostrarSuperaCant(self,xcant):
        for i in len(self.__listaE):
            if type(self.__listaE[i]) == Concierto:
                if self.__listaE[i].getCantM() > xcant:
                    print(f"""
                       Nombre: {self.__lista[i].getNombre()}
                       Fecha: {self.__lista[i].getFecha()}
                       Precio Final: {self.__lista[i].precioEntrada()}
                       """)                                                                           