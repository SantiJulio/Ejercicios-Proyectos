from Tramo import Tramo
import csv

class GestorTramo:
    __lista: list

    def __init__(self):
        self.__lista = []

    def cargaGestorTramo(self,tramo):
        self.__lista.append(tramo)

    def leerTramo(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Empresa de Transporte/tramos.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unTramo = Tramo(fila[0], fila[1], float(fila[2]), fila[3])
                self.cargaGestorTramo(unTramo)
    
    def mostrarDatosPorPatente(self,patente):
        acum = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].getPatenteC() == patente:
                print(f"""
                       Ciudad origen {self.__lista[i].getCiudadO()}
                       Ciudad Destino {self.__lista[i].getCiudadD()}
                       Distancia {self.__lista[i].getDistancia()}
                       """)                
                acum += self.__lista[i].getDistancia()   
        print(f"La distancia total del bondi con {patente} es de {acum}")                           

    def totalKilometros(self, patente):
        total = 0
        for tramo in self.__lista:
            if tramo.getPatenteC() == patente:
                total += tramo.getDistancia()
        return total
    
    def listarTramos(self, distancia_limite):
        hay_tramos = False
        for tramo in self.__lista:
            if tramo > distancia_limite: #se activa el __gt__
                print(f"{tramo.getCiudadO():<15} {tramo.getCiudadD():<15} {tramo.getPatenteC():<10} {tramo.getDistancia():<10}")
                hay_tramos = True
        if not hay_tramos:
            print("No hay tramos que superen esa distancia.")        