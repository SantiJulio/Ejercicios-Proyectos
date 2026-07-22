from gestorInmuebles import manejadorInmuebles


def menu():
    ges = manejadorInmuebles()

    bandera = True

    while bandera:
        print("""\n==== MENU DE OPCIONES ====
            1. Agregar Inmueble
            2. Mostrar todos los datos
            3. Mostrar Casas disponibles
            0. Salir del programa
            """)
        try:
            op = input("\nSeleccione una opcion: ")
        except ValueError:
            print("Error: Opcion invalida, intente nuevamente.")

        if op == "1":
            try:
                tipo = input("Tipo de inmueble (1-Casa | 2-Dpto): ")
                ges.cargarInmueble(tipo)
            except TypeError:
                print("\nError: tipo de inmueble desconocido.")

        elif op == "2":
            try:
                cant = int(input("\nIngrese una cantidad de dormitorios: "))
                if cant < 0:
                    raise ValueError
                else:
                    ges.mostrarDepartamentos(cant)
            except ValueError:
                print("\nError: la cantidad de dormitorios debe ser más de 0.")

        elif op == "3":
            ges.mostrarCasas()

        elif op == "0":
            bandera = False
            print("\nSaliendo..")

        else:
            print("\nOpcion invalida, intente nuevamente.")


if __name__ == "__main__":
    menu()
