from GestorMaquina import GestorMaquina
from Tractor import Tractor
from Cosechadora import Cosechadora

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")

if __name__ == '__main__':
    GM = GestorMaquina()
    GM.cargaMaquina()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = input("Seleccione un numero entre (1-4)")
        opcion = int(entrada)
        if opcion == 1:
            xid = int(input("Ingrese un id: "))
            GM.mostrarPorId(xid)
        elif opcion == 2:
            pass                    