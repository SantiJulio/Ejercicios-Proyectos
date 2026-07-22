from GestorHospitales import GestorHospitales
from ClaseServicio import Servicio
import numpy as np

class GestorServicios:
    __ndarray: np.ndarray
    __dimension: int
    __cantidadOcupadas: int
    __incremento: int
    def __init__(self, dimension = 6, incremento = 6):
        self.__ndarray = np.empty(dimension, dtype = Servicio)
        self.__incremento = incremento
        self.__cantidadOcupadas = 0
        self.__dimension = dimension
    def cargaGestorServicios(self, servicio):
        if self.__dimension == self.__cantidadOcupadas:
            self.__dimension += self.__incremento
            self.__ndarray = np.resize(self.__ndarray, self.__dimension)
        self.__ndarray[self.__cantidadOcupadas] = servicio
        self.__cantidadOcupadas += 1
    def buscarServicio(self, nombre, gestorHospitales):
        i = 0
        while i < self.__cantidadOcupadas and self.__ndarray[i].getNombre() != nombre:
            i += 1
        if i < self.__cantidadOcupadas:
            codHospital = self.__ndarray[i].getCodHospital()       
            gestorHospitales.buscarHospitalPorCod(codHospital)
        else:
            print("Servicio no encontrado")
    def acumuladorServiciosHospital(self, codHospital):
        acumulador = 0
        for servicio in self.__ndarray:
            if servicio.getCodHospital() == codHospital:
                acumulador += 1
        return acumulador
    def mostrarEspecialidad(self, especialidad, gestorHospitales):
        for servicio in self.__ndarray:
            if servicio.getEspecialidad() == especialidad:
                print(f"Nombre del servicio {servicio.getNombre()}")
                gestorHospitales.buscarHospitalPorCod(servicio.getCodHospital())
    def listarOrdenado(self, codHospital):
        self.__ndarray.sort()
        print("Listado ordenado alfabeticamente por nombre")
        for servicio in self.__ndarray:
            if servicio.getCodHospital() == codHospital:
                print(servicio)