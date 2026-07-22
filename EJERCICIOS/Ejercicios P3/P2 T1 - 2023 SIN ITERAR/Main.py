from GestorInmueble import Gestor
from Casa import Casa
from Departamento import Departamento

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")

if __name__ == '__main__':
    GI = Gestor()
    GI.cargaInmueble()
    opcion = 0
    while opcion != 6:
        mostrarMenu()
        entrada = int(input("Seleccione una opcion entre (1-5): "))
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                xtipo = input("Ingrese tipo de Inmueble: ")
                xloc = input("Ingrese localidad: ")
                xdir = input("Ingrese direccion: ")
                xsup = float(input("Ingrese superficie: "))
                if xtipo == "C":
                    xmetro = float(input("Ingrese metros: "))
                    unInmueble = Casa(xloc,xdir,xsup,xmetro)
                    GI.agregarInmueble(unInmueble)
                elif xtipo == 'D':
                    xcantD = int(input("Ingrese cantidad de dormitorios: "))
                    xnroM = int(input("Ingrese nro de mono: "))
                    xnroD = int(input("Ingrese nro de departamento: "))
                    xpiso = int(input("Ingrese piso: "))
                    unInmueble = Departamento(xloc,xdir,xsup,xcantD,xnroM,xnroD,xpiso)
                    GI.agregarInmueble(unInmueble)            
            elif opcion == 3:
                xcD = int(input("Ingrese una cantidad de dormitorios: "))
                GI.mostrarPorDormi(xcD)
            elif opcion == 4:
                GI.mostrarCasa()                        