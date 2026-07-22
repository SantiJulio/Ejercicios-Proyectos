from GestorEvento import GestorEvento

def mostrarMenu():
    print("\n" + "="*20)
    print(" MENU PRINCIPAL")
    print("="*20)
    print("1- .")
    print("2- .")
    print("3- .")
    print("4- .")
    print("5- .")
    print("6- SALIR")
    print("="*20)

if __name__ == '__main__':
    GE = GestorEvento()
    GE.cargaEvento()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-5): ")
        opcion = int(entrada)
        if opcion == 1:
            id = int(input("Ingrese un id: "))
            nombreE = input("Ingrese un nombre de evento: ")
            fecha = input("Ingrese una fecha: ")
            tipo = input("Ingrese un tipo: ")
            GE.agregarEvento(id,nombreE,fecha,tipo)
        elif opcion == 2:
            idE = int(input("Ingrese un id de evento: "))
            nombreI = input("Ingrese nombre de invitado: ")
            dni = int(input("Ingrese un dni: "))
            email = input("Ingrese un email: ")
            dir = input("Ingrese una direccion: ")
            GE.agregarInvitadoEvento(idE,nombreI,dni,email,dir)                   
        elif opcion == 3:
            xtipo = input("Ingrese un tipo de Evento: ")
            GE.mostrarNombreInvitado(xtipo)    
        elif opcion == 4:
            xdni = int(input("Ingrese un dni: "))
            GE.mostrarRegistrado(xdni)
        elif opcion == 5:
            xfecha = input("Ingrese una fecha: ")
            GE.mostrarPorFecha(xfecha)    