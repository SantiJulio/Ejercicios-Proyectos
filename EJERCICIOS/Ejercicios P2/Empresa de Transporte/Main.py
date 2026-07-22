from GestorColectivo import GestorColectivo
from GestorTramo import GestorTramo

def mostrarMenu():
    print("\n" + "="*20)
    print("  MENU PRINCIPAL")
    print("="*20)
    print("1- Ingrese un Numero de DNI de un Chofer para Mostrar los Tramos Recorridos por el Chofer.")
    print("2- Mostrar por cada Colectivo la Cantidad de KM recorridos y el gasto estimado de combustible para la cantidad de km recorridos.")
    print("3- Ingrese una Distancia Recorrida para Informar los Tramos en los que los km recorridos superan la distancia dada.")
    print("4- SALIR")
    print("="*20)


if __name__ =='__main__':
    cantidad = int(input("Ingrese la Cantidad de Colectivos: "))
    GC = GestorColectivo(cantidad)
    GC.leerColectivo()
    GT = GestorTramo()
    GT.leerTramo()
    opcion = 0
    while opcion != 4:
        mostrarMenu()
        entrada = input("Seleccione una opcion (1-4): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                xdni = int(input("Ingrese DNI de un chofer: "))
                GC.listadoTramos(GT,xdni)
            elif opcion == 2:
                GC.mostrarGastoTotal(GT) 
            elif opcion == 3:
                dist = float(input("Ingrese una distancia a superar: "))
                GT.listarTramos(dist)
            elif opcion == 4:
                print ("Saliendo del Sitema...\n")
            else:
                print("Opcion NO valida, Por favor, elija un numero entre 1-4: ")
        else:
            print("Entrada Invaldia. Por Favor, ingrese un numero.")   