from GestorHos import GestorHos
from GestorServ import GestorServ
from Hospitales import Hospital
from Servicios import Servicio
import csv

def test():
    gestorHos = GestorHos()
    archivo = open("EJERCICIOS\Ejercicios P2\Ministerio de Salud/Hospitales.csv")
    reader = csv.reader(archivo, delimiter = ";")
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
            hospital = Hospital(id,nombre,direccion,localidad,telefono)
            gestorHos.cargaGestorHos(hospital)

    gestorServ = GestorServ()
    archivo = open("EJERCICIOS\Ejercicios P2\Ministerio de Salud/Servicios.csv")
    reader = csv.reader(archivo, delimiter = ";")
    next(reader) #Puede saltar la lista completa
    for fila in reader:
        id = int(fila[0])
        nombre = fila[1]
        especialidad = fila[2]
        horario = fila[3]
        idHospital = int(fila[4])
        servicio = Servicio(id,nombre,especialidad,horario,idHospital)
        gestorServ.cargaGestorServ(servicio)
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
            gestorServ.buscarServicio(nombre, gestorHos)
        case "B":
            gestorHos.cantidadServ(gestorServ)             