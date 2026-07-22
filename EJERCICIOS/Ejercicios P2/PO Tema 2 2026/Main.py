from GestorAspirante import GestorAspirante
from GestorInscripcion import GestorInscripcion

def mostrarMenu():
    print("\n" + "="*20)
    print(" MENU PRINCIPAL")
    print("="*20)
    print("1- Leer los datos de los archivos.")
    print("2- Ingrese por teclado un dni y mostra nombre, apellido y telefono, indicando si posee o no inscripciones a mas de un curso. Mostrar id y descripciones de los cursos.")
    print("3- Ingrese por teclado un dni y un id mostrar su nya, si esta inscripto mas de una vez al mismo curso, mostrar nombre, apellido, telefono, fecha y descripcion.")
    print("4- Ingrese por teclado un id ")
    print("5- Ingrese por teclado un dni, mostrar apellido, nombre, telefono y el importe por e curso que tiene beca aceptada.")
    print("6- SALIR")
    print("="*20)

if __name__ == '__main__':
    GA = GestorAspirante()
    GI = GestorInscripcion()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-6): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                GA.leerAspirante()
                GI.leerInscripcion()
            if opcion == 2:
                xdni = int(input("Ingresa un DNI: "))
                GA.mostrarNomApeTel(xdni,GI)  
            if opcion == 3:
                xxdni = int(input("Ingresar otro DNI: "))
                xid = int(input("Ingresar id: "))
                GI.InscEnUnMismoCurso(xxdni,xid,GA)   