from Hospitales import Hospital
import csv

class GestorHos:
    __lista: list

    def __init__(self):
        self.__lista = []

    def cargaGestorHos(self, hospital):
        self.__lista.append(hospital)

    def buscarHosPorCod(self, codigo):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getCodigo() != codigo:
            i += 1
        if i < len(self.__lista):
            print(f"El nombre del hospital es {self.__lista[i].getNombre()}")
        else:
            print("Codigo del hospital no encontrado.") 

    def cantidadServ(self,gestorServ):
        for hospital in self.__lista:
                               