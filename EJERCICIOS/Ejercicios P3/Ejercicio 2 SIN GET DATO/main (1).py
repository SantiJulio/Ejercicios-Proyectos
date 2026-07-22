from gestorEventos import GestorEventos


def menu():
    print("####################################")
    print("1. Mostrar eventos")
    print("2. Agregar evento")
    print("3. Agregar invitado")
    print("4. Mostrar invitados por tipo de evento")
    print("5. Mostrar eventos de un invitado")
    print("6. Mostrar conferncias por fecha")
    print("7. Salir")
    print("8. ")
    print("####################################")


if __name__ == "__main__":
    ge = GestorEventos()
    ge.cargar_eventos()
    ge.cargar_invitados()

    menu()
    opc = int(input("Ingrese una opcion: "))

    while(opc != 7):
        match opc:
            case 1:
                ge.mostrar_eventos()

            case 2:
                id = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                fecha = input("Ingrese fecha: ")
                tipo = input("Ingrese tipo: ")

                ge.agregar_evento(id, nombre, fecha, tipo)

            case 3:
                id_evento = int(input("Ingrese ID de evento: "))
                nombre = input("Ingrese nombre: ")
                dni = int(input("Ingrese DNI: "))
                email = input("Ingrese email: ")
                direccion = input("Ingrese direccion: ")

                ge.agregar_invitado(id_evento, nombre, dni, email, direccion)


            case 4:
                tipo = input("Ingrese tipo: ")
                ge.mostrar_invitados_por_tipo(tipo)

            case 5:
                dni = int(input("Ingrese DNI: "))
                ge.mostrar_eventos_por_invitado(dni)

            case 6:
                fecha = input("Ingresar fecha: ")
                ge.mostrar_conferencias(fecha)

            case 7:
                pass
            case _:
                print("Opcion invalida")

        menu()
        opc = int(input("Ingrese una opcion: "))

