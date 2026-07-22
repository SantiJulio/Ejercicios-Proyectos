from GestorComplejo import Gestor

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")

if __name__ == '__main__':
    GC = Gestor()
    GC.cargaComplejo()
    GC.cargaCabaña()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = int(input("Seleccione una opcion entre (1-5): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                xplanta = input("Ingrese una planta: ")
                GC.mostrarPorPlanta(xplanta)  
            elif opcion == 2:
                xid = input("Ingrese id de complejo: ")
                xnro = int(input("Ingrese nro de unidad: "))
                xcantDias = int(input("Ingrese cantidad de dias: "))      
                GC.mostrarPorIdNroCant(xid,xnro,xcantDias)
            elif opcion == 3:
                GC.mostrarPorComplejo() 
            elif opcion == 4:
                GC.calcularPorComplejo(xid)
            elif opcion == 5:
                pos = int(input("Ingrese posicion: "))
                try:
                    GC.mostrarPorPos(pos)
                except IndexError as e:
                    print(f"Error: {e}")               