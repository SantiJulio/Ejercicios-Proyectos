from Aspirante import Aspirante
import csv

class GestorAspirante:
    __lista: list

    def __init__(self):
        self.__lista = []

    def cargaAspirante(self,aspirante):
        self.__lista.append(aspirante)

    def leerAspirante(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/PO Tema 2 2026/aspirantesBecas.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            next(reader)
            for fila in reader:
                unAspirante = Aspirante((int(fila[0])), fila[1], fila[2], fila[3], fila[4], (int(fila[5])))
                self.cargaAspirante(unAspirante)
    
    def mostrarNomApeTel(self,xdni,gestorInscripcion):
        i = 0
        encontrado = False
        dni = None
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getDni() == xdni:
                encontrado = True
                dni = self.__lista[i].getDni()
            else:
                i+=1
        if encontrado:
            print(f"""
                   Nombre {self.__lista[i].getNombre()}
                   Apellido {self.__lista[i].getApellido()}
                   Telefono {self.__lista[i].getTelefono()}
                   """)
            gestorInscripcion.mostrarInscMasUnCurso(dni)    

    def mostrarCosas(self,dni):
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni() == dni:
                print(f"""
                       Nombre {self.__lista[i].getNombre()}
                       Apellido {self.__lista[i].getApellido()}
                       Telefono {self.__lista[i].getTelefono()}
                       """)           