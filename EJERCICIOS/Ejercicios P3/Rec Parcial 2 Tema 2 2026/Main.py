from GestorCurso import Gestor

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")

if __name__ == '__main__':
    GC = Gestor()
    GC.cargaCurso()
    GC.cargaEstudiante()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = int(input("Seleccione un numero entre (1-5): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                auxId = int(input("Ingrese curso al que desea ingresar: "))
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese Apellido: ")
                dni = int(input("Ingrese dni: "))
                correo = input("Ingrese correo: ")
                ciudad = input("Ingrese ciudad: ")
                GC.instanciarEstudiante(auxId,nombre,apellido,dni,correo,ciudad)        
            elif opcion == 2:
                xdni = int(input("Ingrese un dni: "))
                GC.buscarEst(xdni) 
            elif opcion == 3:
                xcat = input("Ingrese categoria: ")
                GC.buscarCat(xcat)       
            elif opcion == 4:
                xd = int(input("Ingrese dni: "))
                GC.buscar(xd)
            elif opcion == 5:
                pos = int(input("Ingrese una posicion: "))
                try:
                    GC.validarPos(pos)
                except IndexError as e:
                    print(f"Posicion invalida: {e}")
