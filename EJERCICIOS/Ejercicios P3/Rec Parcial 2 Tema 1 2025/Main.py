from GestorEmbarcacion import GestorEmbarcacion
from Velero import Velero
from Lancha import Lancha

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GE = GestorEmbarcacion()
    GE.cargaEmbarcacion()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-4): ")
        opcion = int(entrada)
        if opcion == 1:
            nom = input("Ingrese nombre de embarcacion: ")
            tipo = input("Ingrese tipo de embarcacion: ")
            eslora = float(input("Ingrese eslora: "))
            anio = int(input("Ingrese anio: "))
            costo = float(input("Ingrese costo: "))
            dispo = input("¿Hay disponibilidad? (True or False)")
            dispo = True if dispo.lower() == 'true' else False
            cantD = int(input("Ingrese cantidad de dias: "))
            if tipo == 'Velero':
                cantV = int(input("Ingrese cantidad de velas: "))
                embarcacion = Velero(cantV,nom,eslora,anio,costo,dispo,cantD) 
                GE.crearYagregarEmbar(embarcacion)
            elif tipo == 'Lancha':
                potencia = float(input("Ingrese potencia: "))
                embarcacion = Lancha(potencia,nom,eslora,anio,costo,dispo,cantD)
                GE.crearYagregarEmbar(embarcacion)      
        elif opcion == 2:
            xnom = input("Ingrese un nombre de embarcacion: ")
            GE.alquilar(xnom)        
        elif opcion == 3:
            GE.mostrarAlquilado() 
        elif opcion == 4:
            GE.mostrarDisponible()       