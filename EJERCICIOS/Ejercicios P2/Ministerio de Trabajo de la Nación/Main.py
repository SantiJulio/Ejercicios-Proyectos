from GestorCurso import GestorCurso
from GestorInscripcion import GestorInscripcion

def mostrarMenu():
    print("\n" + "="*20)
    print(" MENU PRINCIPAL")
    print("="*20)
    print("1- Ingrese por teclado un numero de DNI, obtenga la primera inscripción que coincide con dicho DNI, y recorrer el manejador buscando inscripciones repetidas, y las ponga en estado Rechazada.")
    print("2- Leer desde teclado un identificador de curso, y procesar las inscripciones.")
    print("3- Obtener un listado por curso, de las inscripciones rechazadas ordenada alfabéticamente.")
    print("4- Leer un identificador de curso, y listar los inscriptos que fueron aceptados en dicho curso.")
    print("5- SALIR")
    print("="*20)

if __name__ == '__main__':
    GC = GestorCurso()
    GC.leerCurso()
    GI = GestorInscripcion() 
    GI.leerInscripcion()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-5): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                xdni = int(input("Ingrese DNI: "))
                GI.procesarInscripcionesRepetidas(xdni)   
            elif opcion == 2:
                xid = int(input("Ingrese un identificador de curso: "))
                curso = GC.buscarCursoPorId(xid) #Buscamos primero el objeto curso para conocer sus cupos
                GI.procesarCupos(xid, curso)
            elif opcion == 3:
                GC.generarReporteRechazados(GI) 
            elif opcion == 4:
                xidCurso = int(input("Ingrese un identificador de curso para ver los aceptados: "))
                GI.generarReporteAceptados(xidCurso) 
            elif opcion == 5:
                print ("Saliendo del Sitema...\n")
            else:
                print("Opcion NO valida, Por favor, elija un numero entre 1-5: ")
        else:
            print("Entrada Invaldia. Por Favor, ingrese un numero.")