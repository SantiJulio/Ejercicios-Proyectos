from GestorEvento import GestorEvento

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")

if __name__ == '__main__':
    GE = GestorEvento()
    GE.cargaEvenInv()
    opcion = 0
    if opcion != 6:
        mostrarMenu()
        entrada = int(input("Seleccione una opcion entre (1-5): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                idE = int(input("Ingrese un id de evento: "))
                nomE = input("Ingrese un nombre de evento:")
                fecha = input("Ingrese una fecha: ")
                tipo = input("Ingrese un tipo: ")
                try:
                    GE.agregarEv(idE,nomE,fecha,tipo)
                except ValueError as e:
                    print("Error: {e}")
            elif opcion == 2:
                id = int(input("Ingrese id: "))
                nomI = input("Ingrese nombre del invitado: ")
                dni = int(input("Ingrese dni: "))
                email = input("Ingrese el mail: ")
                dir = input("Ingrese la direccion: ")
                GE.agregarIn(id,nomI,dni,email,dir)            
            elif opcion == 3:
                xtipo = input("Ingrese tipo de evento a evaluar: ")
                GE.mostrarPorTipo(xtipo) 
            elif opcion == 4:
                xdni = int(input("Ingrese dni: "))
                GE.mostrarPorDni(xdni)       