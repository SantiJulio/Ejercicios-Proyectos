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
    GC.cargaCliYCons()
    opcion = 0
    while opcion != 7:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-6): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                idC = int(input("Ingrese id del consultorio: "))
                nroC = int(input("Ingrese numero del consultorio: "))
                piso = int(input("Ingrese piso: "))
                esp = input("Ingrese especialidad: ")
                costo = float(input("Ingrese costo diario: "))
                estado = input("Ingrese estado: ")
                GC.agregarConsulCli(idC,nroC,piso,esp,costo,estado)     
            elif opcion == 2:
                xnum = int(input("Ingrese un numero: "))
                GC.registrarOcupado(xnum)
            elif opcion == 3:
                GC.registrarLibre(xnum)  
            elif opcion == 4:
                xe = input("Ingrese una especialidad: ")
                GC.mostrarMenorMayor(xe)
            elif opcion == 5:
                xnom = input("Ingrese nombre: ")
                GC.cantidadLibre(xnom) 
            elif opcion == 6:
                GC.mostrarPorEsp()                 