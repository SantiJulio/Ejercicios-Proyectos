from GestorHospitales import GestorHospitales
from GestorServicios import GestorServicios
from ClaseHospital import Hospital
from ClaseServicio import Servicio
import csv

def test():
    gestorHospitales = GestorHospitales()
    archivo = open("Unidad1/Ej6/Hospitales.csv")
    reader = csv.reader(archivo, delimiter = ';')
    bandera = True
    for fila in reader:
        if bandera == True:
            bandera = False
            print("Se omite la primer fila del reader") 
        else:
            id = int(fila[0])
            nombre = fila[1]
            direccion = fila[2]
            localidad = fila[3]
            telefono = fila[4]
            hospital = Hospital(id, nombre, direccion, localidad, telefono)
            gestorHospitales.cargaGestorHospitales(hospital)
    
    gestorServicios = GestorServicios()
    archivo = open("Unidad1/Ej6/Servicios.csv")
    reader = csv.reader(archivo, delimiter = ';')
    next(reader) #Puede saltar la lista completa
    for fila in reader:
        id = int(fila[0])
        nombre = fila[1]
        especialidad = fila[2]
        horario = fila[3]
        idHospital = int(fila[4])
        servicio = Servicio(id, nombre, especialidad, horario, idHospital)
        gestorServicios.cargaGestorServicios(servicio)
    opcion = input(""" 
                Ingrese una opcion:
                A - Inciso a
                B - Inciso b
                C - Inciso c
                D - Inciso d
                E - Inciso e
                    """)
    match opcion.upper():
        case "A":
            nombre = input("Ingrese el nombre de un servicio: ")
            gestorServicios.buscarServicio(nombre, gestorHospitales)
        case "B":
            gestorHospitales.cantidadServicios(gestorServicios)
        case "C":
            gestorHospitales.maxCantServicios(gestorServicios)
        case "D":
            nombre = input("Ingrese un nombre de especialidad: ")
            gestorServicios.mostrarEspecialidad(nombre, gestorHospitales)
        case "E":
            nombre = input("Ingrese un nombre de hospital: ")
            gestorHospitales.buscarHospitalPorNombre(nombre,gestorServicios)
        case _:
            print("Opcion invalida")