from Maquina import Maquina
from Cosechadora import Cosechadora
from Tractor import Tractor
import csv

class GestorMaquina:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarMaquina(self,maquina):
        if not isinstance(maquina, Maquina):
            raise TypeError("El objeto no pertenece a la jerarquía Maquina.")
        self.__lista.append(maquina)

    def cargaMaquina(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Parcial 2 Tema 2 2026/maquinaria.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                tipo = fila[0]
                id = int(fila[1])
                marca = fila[2]
                modelo = fila[3]
                anio = int(fila[4])
                precio = float(fila[5])
                if tipo == 'T':
                    potencia = float(fila[6])
                    tipoT = fila[7]
                    maquina = Tractor(potencia,tipoT,id,marca,modelo,anio,precio)
                elif tipo == 'C':
                    capac = int(fila[8])
                    tipoC = fila[9]
                    maquina = Cosechadora(capac,tipoC,id,marca,modelo,anio,precio)
                self.agregarMaquina(maquina)   
            try:
                self.agregarMaquina(maquina)
            except TypeError as e:
                print(e)  

    def mostrarPorId(self,xid):
        i = 0
        encontrado = False
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getId == xid:
                encontrado = True
                if isinstance(self.__lista[i],Tractor):  
                    print(f"""
                        Marca: {self.__lista[i].getMarca()} 
                        Potencia: {self.__lista[i].getPotencia()}
                        Traccion: {self.__lista[i].getTipoT()}
                        """)                        
                elif isinstance(self.__lista[i],Cosechadora):
                    print(f"""
                        Marca: {self.__lista[i].getMarca()}
                        Capacidad: {self.__lista[i].getCapac()}
                        Cabezal: {self.__lista[i].getTipoC()}                      
                        """)    
                else:
                    raise ValueError
            else:
                i += 1

    def mostrarMayorPotencia(self,xpot):
        for i in self.__lista:
            if isinstance(i,Tractor):
                if i.getPotencia() > xpot:
                    print(f"Modelo: {i.getModelo()}")
                else: 
                    print("No supera la potencia ingresada.")
            else:
                print("No es un Tractor.")

    def mostrarTodo(self):
        for i in self.__lista:
            i.mostrarDatos()
    
    def mostrarPosicion(self,pos):
        if pos < 0 or pos >= len(self.__lista):
            raise IndexError
        print(self.__lista[pos])