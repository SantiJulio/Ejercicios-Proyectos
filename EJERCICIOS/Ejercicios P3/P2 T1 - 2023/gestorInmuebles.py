from claseInmuebles import Inmueble
from claseCasas import Casa
from claseDepartamentos import Departamento
from listaDefinida import ListaInmuebles


class manejadorInmuebles:
    __lista: ListaInmuebles

    def __init__(self):
        self.__lista = ListaInmuebles()

    def agregarInmueble(self, nuevoInmueble):
        if isinstance(nuevoInmueble, Inmueble):
            self.__lista.agregar(nuevoInmueble)
        else:
            raise TypeError

    def cargarInmueble(self, xtipo):
        print("\n--DATOS DEL INMUEBLE--")
        loc = input("Localidad: ")
        dir = input("Direccion: ")
        sup = float(input("Superficie Cubierta: "))

        if xtipo == "1":
            print("\nTipo -> CASA")
            mts = float(input("Metros cuadrados del terreno: "))
            nuevo = Casa(loc, dir, sup, mts)
            self.agregarInmueble(nuevo)

        elif xtipo == "2":
            print("\nTipo -> DEPARTAMENTO")
            cant = int(input("Cantidad de dormitorios: "))
            numMono = int(input("Numero de Monoblock: "))
            numDp = int(input("Numero de Departamento: "))
            piso = int(input("Piso: "))
            nuevo = Departamento(loc, dir, sup, cant, numMono, numDp, piso)
            self.agregarInmueble(nuevo)

        else:
            raise TypeError

    def mostrarCasas(self):
        for inm in self.__lista:
            print("\n--CASAS a la venta--")
            if isinstance(inm, Casa):
                print("\n--CASAS A LA VENTA--")
                print(inm)

    def mostrarDepartamentos(self, xcant):
        for inm in self.__lista:
            if isinstance(inm, Departamento):
                if inm.getCantidadDormitorios() < xcant:
                    print(inm)
