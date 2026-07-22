from GestorReceta import GestorReceta

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GR = GestorReceta()
    GR.cargaRecIng()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-4): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                id = int(input("Ingrese un id de receta: "))
                nomI = input("Ingrese un nombre de ingrediente: ")
                unidad = input("Ingrese una unidad: ")
                stock = int(input("Ingrese una cantidad: "))
                GR.agregarIng(id,nomI,unidad,stock)
            elif opcion == 2: 
                xnomR = input("Ingrese un nombre de receta a evaluar: ")
                pos = int(input("Ingrese una posicion: "))
                try:
                    GR.mostrarIng(xnomR,pos)
                except IndexError as e:
                    print(f"Error: {e}") 
            elif opcion == 3:
                xnomI = input("Ingrese Nombre de un ingrediente: ")
                GR.mostrarRec(xnomI)           