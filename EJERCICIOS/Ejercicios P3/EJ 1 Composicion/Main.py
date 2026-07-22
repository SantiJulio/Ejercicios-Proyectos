from GestorClinica import GestorClinica

def mostrarMenu():
    print("\n" + "="*20)
    print(" MENU PRINCIPAL")
    print("="*20)
    print("1- Agregar consultorios a la clinica.")
    print("2- Dado nro de consultorio y registrarlo como ocupado.")
    print("3- Dado nro de consultorio y registrarlo como libre.")
    print("4- Dada una especialidad medica. Mostrar nroC, piso, estado actual, de todos los consultorios que correspondan a dicha especialidad, ordenado de menor a mayor por piso y número de consultorio.")
    print("5- Leer por teclado el nombre de una clinica y mostrar la cantidad de consultorios libres por piso.")
    print("6- Para cada especialidad mostrar el detalle asociado.")
    print("7- SALIR")
    print("="*20)

if __name__ == '__main__':
    GC = GestorClinica()
    GC.cargaClinica()
    opcion = 0
    while opcion != 7:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-6): ")
        opcion = int(entrada)
        if opcion == 1:
            idC = int(input("Ingrese un id de consultorio: "))
            nroC = int(input("Ingrese un nro de consultorio: "))
            piso = int(input("Ingrese un piso: "))
            espec = input("Ingrese una especialidad: ") 
            costo = float(input("Ingrese un costo: "))
            estado = input("Ingrese un estado: ")
            GC.agregarConsultorioClinica(idC,nroC,piso,espec,costo,estado)       
        elif opcion == 2:
            xnroC = int(input("Ingrese un numero de consultorio: "))
            GC.registrarOcupado(xnroC)    
        elif opcion == 3:
            GC.registrarLibre(xnroC)    
        elif opcion == 4:
            xesp = input("Ingresar especialidad de un consultorio: ")    
            GC.mostrarMenorAMayor(xesp)
        elif opcion == 5:
            xnom = input("Ingrese nombre de una clinica: ")
            GC.mostrarCantidadPorPiso(xnom)    
        elif opcion == 6:
            GC.mostrarPorEspecialidad()    