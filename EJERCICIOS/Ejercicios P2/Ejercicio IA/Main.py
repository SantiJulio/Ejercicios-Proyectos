from GestorDrones import gestorDron
from GestorEnvios import gestorEnvio

def mostrarMenu():
    print("\n" + "="*20)
    print("  MENU PRINCIPAL")
    print("="*20)
    print("1- Ingrese un Numero de DNI de un Operador para Mostrar los Envios por sus Drones y el Tiempo Total del Vuelo Acumulado.")
    print("2- Mostrar por cada Dron el tiempo total de vuelo acumulado y el gasto estimado de batería total.")
    print("3- Ingrese un Tiempo de Vuelo para listar los envios cuyo Tiempo supere al Ingresado.")
    print("4- SALIR")
    print("="*20)


if __name__ == '__main__':
    GD = gestorDron()
    GD.leerDrones()
    GE = gestorEnvio()
    GE.leerEnvios()
    opcion = 0 
    while opcion != 4:
        mostrarMenu()
        entrada = (input("Selecciona una opcion(1-4): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                dni = input("Ingrese un DNI para analizar: ")
                GD.listarEinformar(dni,GE)
            if opcion == 2:
                GD.mostrarTiempoGasto(GE)   
            if opcion == 3:
                xtiempo = int(input("Ingresar tiempo de vuelo: "))
                GE.listarEnvios(xtiempo)         
                