from GestorMateria import GestorMateria

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GM = GestorMateria()
    GM.cargaMatYTema()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-5): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                cod = input("Ingrese codigo de materia: ")
                nomM = input("Ingrese nombre de la materia: ")
                desp = input("Ingrese despliegue(Anual o Semestral): ")
                anio = int(input("Ingrese el anio: "))
                GM.agregarMat(cod,nomM,desp,anio)
            elif opcion == 2:
                codM = input("Ingrese codigo: ")
                nomT = input("Ingrese nombre del tema: ")
                desc = input("Ingrese descripcion: ")
                GM.agregarTema(codM,nomT,desc)          
            elif opcion == 3:
                xanio = int(input("Ingrese un anio: "))
                GM.listarMatAnuales(xanio)
            elif opcion == 4:
                xnomT = input("Ingrese nombre de un tema: ")
                GM.mostrar(xnomT)        