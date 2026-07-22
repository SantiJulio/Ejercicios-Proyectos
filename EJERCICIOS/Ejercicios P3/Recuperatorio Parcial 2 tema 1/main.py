from gestorEquipos import Gestor

if __name__ == '__main__':
    gestor = Gestor()
    gestor.cargar()
    
    def menu(opcion, gestor):
        if opcion == 1:
            posicion = int(input("Ingrese la posicion: "))
            try:
                gestor.obtenerPorPosicion(posicion)
            except IndexError:
                print("Índice fuera de rango")            
        elif opcion == 2:
            anio = int(input("Ingrese el año de fabricación: "))
            gestor.contarHerramientaElectrica(anio)
        elif opcion == 3:
            capCarga = int(input("Ingrese la capacidad de carga: "))
            gestor.mostrarMaquinariaPesadaMenorIgual(capCarga)
        elif opcion == 4:
            gestor.mostrarTodosLosEquipos()
        elif opcion == 5:
            print("Saliendo del programa")
        else:
            print("Opcion no valida")
        
    opcion = 0
    while opcion != 5:
        print("1. inciso 1")
        print("2. inciso 2")
        print("3. inciso 3")
        print("4. inciso 4")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        menu(opcion, gestor)
    