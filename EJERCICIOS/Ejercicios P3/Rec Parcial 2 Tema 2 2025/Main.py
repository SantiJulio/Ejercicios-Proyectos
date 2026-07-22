from GestorEspectaculo import GestorEspectaculo
from Obra import Obra
from Concierto import Concierto

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GE = GestorEspectaculo()
    GE.cargaEspectaculo()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = int(input("Seleccione una opcion entre (1-4): "))
        opcion = int(entrada)
        if opcion == 1:
            nom = input("Ingrese nombre del espectaculo: ")
            fecha = input("Ingrese fecha del espectaculo: ")
            precio = float(input("Ingrese precio: "))
            tipo = input("Ingrese tipo de espectaculo: ")
            if tipo == 'ObraTeatro':
                nomD = input("Ingrese nombre del director: ")
                dur = int(input("Ingrese duracion del mismo: "))
                espectaculo = Obra(nomD,dur,nom,fecha,precio) 
                GE.crearYagregarEspec(espectaculo)
            elif tipo == 'Concierto':
                banOart = input("Ingrese banda o artista: ")
                cantM = int(input("Ingrese cantidad de musicos: "))
                espectaculo = Concierto(banOart,cantM,nom,fecha,precio)
                GE.crearYagregarEspec(espectaculo) 
        elif opcion == 2:
            GE.mostrarTodos()
        elif opcion == 3:
            GE.listarSuperior()
        elif opcion == 4:
            xcant = int(input("Ingrese cantidad de musicos: "))
            GE.mostrarSuperaCant(xcant)                      