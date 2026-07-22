from MaterialPrestado import MaterialPrestado
import csv
import numpy as np

class GestorMaterialPrestado:
    arreglo: np.ndarray
    dimension: int
    cantidad: int
    incremento: int

    def __init__(self,dimension=5,incremento=5):
        self.__arreglo = np.empty(dimension, dtype=MaterialPrestado)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = incremento

    def cargaMaterialP(self,materialP):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arreglo = np.resize(self.__arreglo, self.__dimension) 
        self.__arreglo[self.__cantidad] = materialP
        self.__cantidad += 1  

    def leerMaterialP(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/PO Tema 1 2026/materialprestado.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unMaterialP = MaterialPrestado(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]))
                self.cargaMaterialP(unMaterialP)

    def listarPorFechaDevolucion(self,fecha,gestorSolicitante):
        for i in range(self.__cantidad):
            if self.__arreglo[i].getFechaD() == fecha:
                dni = self.__arreglo[i].getDniS()
                for j in range(len(gestorSolicitante.getLista())):
                    if gestorSolicitante.getLista()[j].getDni() == dni:
                        print(f"""
                              Descripcion:{self.__arreglo[i].getDescripcion()}
                              Nombre y Apellido:{gestorSolicitante.getLista()[j].getNyA()}
                              Dni:{dni}
                              Telefono:{gestorSolicitante.getLista()[j].getTelefono()}
                              """)

    def mostrarPorDniSoli(self,xdni,gestorSolicitante):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__arreglo[i].getDniS() == xdni:
                encontrado = True
            else:
                i+=1
        if encontrado:
            for j in range(len(gestorSolicitante.getLista())):
                if gestorSolicitante.getLista()[j].getDni() == xdni:
                    print(f"""
                            Nombre y Apellido:{gestorSolicitante.getLista()[j].getNyA()}
                            Descripcion:{self.__arreglo[j].getDescripcion()}
                            Garantia:{self.__arreglo[j].getGarantia()}
                            """)
        else:
            print("No se encontro el dni")

    def mostrarPorIdFechaD(self,xid,xfechaD,gestorSolicitante):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__arreglo[i].getId() == xid and self.__arreglo[i].getFechaD() == xfechaD:
                encontrado = True
                dni = self.__arreglo[i].getDniS()
            else:
                i+=1
        if encontrado:
            for j in range(len(gestorSolicitante.getLista())):
                if gestorSolicitante.getLista()[j].getDni() == dni:
                    print(f"""
                          Nombre y Apellido:{gestorSolicitante.getLista()[j].getNyA()}
                          Identificador:{self.__arreglo[j].getId()}
                          Garantia:{self.__arreglo[j].getGarantia()}
                          """)
                GOD = self.__arreglo[j]   
                if GOD == 'Devuelto':
                    GOD.setEstado('No devuelto')
                    GOD.setFechaD('')
        print(f"Nuevo estado: {GOD.getEstado()}")   
        print(f"Nueva Fecha Devolucion: {GOD.getFechaD()}")  

    def mostrarPorIdMP(self,xxid,gestorSolicitante):
        i = 0
        encontrado = False
        contador = 0
        while i < self.__cantidad and not encontrado:
            if self.__arreglo[i].getId() == xxid:
                encontrado = True
                dni = self.__arreglo[i].getDniS()
            else:
                i+=1     
        if encontrado:
            for j in range(self.__cantidad):
                matepres = self.__arreglo[j]
                if matepres.getDniS() == dni and matepres.getId() == xxid:
                    contador+=1
            print(contador)        
            if contador > 1:
                solicitante = None
                k = 0
                while k < len(gestorSolicitante.getLista()) and solicitante is None:
                    if gestorSolicitante.getLista()[k].getDni() == dni:
                        solicitante = gestorSolicitante.getLista()[k]
                    k+=1
                if solicitante is not None:    
                    print(f"""
                           Nombre y Apellido:{solicitante.getNyA()}
                           Dni:{dni}
                           """)
            else:
                print("El id no fue prestado mas de una vez")        