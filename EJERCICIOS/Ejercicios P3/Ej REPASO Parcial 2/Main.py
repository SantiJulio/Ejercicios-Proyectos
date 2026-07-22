from GestorVehiculo import GestorVehiculo
from VehiculoAplicacion import VehiculoAplicacion
from VehiculoSucursal import VehiculoSucursal

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")

if __name__ == '__main__':
    GV = GestorVehiculo()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = input("Seleccione una opcion(1-5): ")
        opcion = int(entrada)
        if opcion == 1:
            tipo = input("Ingrese un tipo de Vehiculo: ")
            cod = input("Ingrese un codigo de auto: ")
            marca = input("Ingrese una marca: ")
            modelo = input("Ingrese un modelo: ")
            precio = float(input("Ingrese precio: "))
            cantD = int(input("Ingrese la cantidad disponible: "))
            if tipo == 'Aplicacion':
                url = input("Ingrese url: ")
                porcD = int(input("Ingrese porcentaje de descuento: "))
                seguro = input("¿Tiene seguro?")
                seguro = True if seguro.lower() == 'true' else False
                costo = float(input("Ingrese el costo: "))
                vehiculo = VehiculoAplicacion(url,porcD,seguro,costo,cod,marca,modelo,precio,cantD)
                GV.agregarVehiculo(vehiculo)
            elif tipo == 'Sucursal':
                dir = input("Ingrese direccion: ")
                porcR = int(input("Ingrese porcentaje de recargo: "))
                vehiculo = VehiculoSucursal(dir,porcR,cod,marca,modelo,precio,cantD)
                GV.agregarVehiculo(vehiculo)
        elif opcion == 2:
            codigo = input("Ingrese codigo a evaluar: ")
            GV.alquilar(codigo)                        
        elif opcion == 3:
            GV.mostrarTodo()
        elif opcion == 4:
            GV.mostrarTodoDosPuntoCero()    
        elif opcion == 5:
            GV.calcularEinformar()
        elif opcion == 6:
            GV.buscarPorCod(codigo)    