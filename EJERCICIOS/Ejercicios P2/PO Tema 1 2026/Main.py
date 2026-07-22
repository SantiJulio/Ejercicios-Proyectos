from GestorSolicitante import GestorSolicitante
from GestorMaterialPrestado import GestorMaterialPrestado

def mostrarMenu():
    print("\n" + "="*20)
    print(" MENU PRINCIPAL")
    print("="*20)
    print("1- Leer los datos de los archivos.")
    print("2- Ingrese por teclado una fecha y listar la descripcion, dni, nya y telefono de los Solicitantes, que tienen que devolver materiales en esa fecha.")
    print("3- Ingrese por teclado un numero de dni y mostrar su nya, garantia (si corresponde).")
    print("4- Ingrese por teclado un id y fecha devolucion, mostrar nya, garantia (si corresponde) y modificar el estado y fecha de devolucion.")
    print("5- Ingrese por teclado un id, e indicar si ha sido prestado mas de una vez a un mismo solicitante. Mostrar dni, nya del Solicitante.")
    print("6- SALIR")
    print("="*20)

if __name__ == '__main__':
    GS = GestorSolicitante()
    GMP = GestorMaterialPrestado()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre 1-6: ")
        if entrada.isnumeric():
            opcion = int(entrada) 
            if opcion == 1:
                GS.leerSolicitante()
                GMP.leerMaterialP()
            elif opcion == 2:
                xfecha = input("Seleccione una fecha de devolucion: ")
                GMP.listarPorFechaDevolucion(xfecha,GS)
            elif opcion == 3:
                xdni = int(input("Ingrese un dni de solicitante: ")) 
                GMP.mostrarPorDniSoli(xdni,GS)
            elif opcion == 4:
                xid = input("Ingrese identificador: ")
                xfechaD = input("Ingrese fecha de devolucion: ")
                GMP.mostrarPorIdFechaD(xid,xfechaD,GS)
            elif opcion == 5:
                xxid = input("Ingrese otro identificador: ")
                GMP.mostrarPorIdMP(xxid,GS)
            elif opcion == 6:
                print ("Saliendo del Sitema...\n")
            else:
                print("Opcion NO valida, Por favor, elija un numero entre 1-5: ")
        else:
            print("Entrada Invaldia. Por Favor, ingrese un numero.")