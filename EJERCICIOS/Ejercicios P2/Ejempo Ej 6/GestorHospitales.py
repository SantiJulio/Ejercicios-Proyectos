from ClaseHospital import Hospital
import csv

class GestorHospitales:
    __lista: list
    def __init__(self):
        self.__lista = []
    def cargaGestorHospitales(self, hospital):
        self.__lista.append(hospital)
    def buscarHospitalPorCod(self, codigo):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getCodigo() != codigo:
            i += 1
        if i < len(self.__lista):
            print(f"El nombre del hospital es {self.__lista[i].getNombre()}")
        else:
            print("Codigo de hospital no encontrado")
    def cantidadServicios(self, gestorServicios):
        for hospital in self.__lista:
            acumulador = gestorServicios.acumuladorServiciosHospital(hospital.getCodigo())
            print(f"La cantidad de servicios que brinda el hospital {hospital.getNombre()} es de {acumulador}")
    def maxCantServicios(self, gestorServicios):
        max = -1
        for hospital in self.__lista:
            acumulador = gestorServicios.acumuladorServiciosHospital(hospital.getCodigo())
            if acumulador > max:
                max = acumulador
                nombreMax = hospital.getNombre()
        print(f"El hospital con mayor cantidad de servicios es {nombreMax} y tiene {max} servicios")
    def buscarHospitalPorNombre(self, nombre, gestorServicios):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getNombre() != nombre:
            i += 1
        if i < len(self.__lista):
            gestorServicios.listarOrdenado(self.__lista[i].getCodigo())
        else:
            print("Nombre de hospital no encontrado")
            
