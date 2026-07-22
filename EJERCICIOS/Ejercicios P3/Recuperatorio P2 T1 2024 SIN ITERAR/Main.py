from GestorEquipo import GestorEquipo

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GE = GestorEquipo()
    GE.cargaEquipo()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = int(input("Seleccione una opcion entre (1-4): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                pos = int(input("Ingrese una posicion: "))
                try:
                    GE.mostrarPorPos(pos)
                except ValueError as e:
                    print(f"Indice fuera de rango: {e}")
            elif opcion == 2:
                xa = int(input("Ingrese anio: "))
                GE.mostrarPorAnio(xa)      
            elif opcion == 3:
                xcapac = int(input("Ingrese una capacidad de carga: "))
                GE.mostrarPorCapac(xcapac)
            elif opcion == 4:
                GE.mostrarTodo()                      