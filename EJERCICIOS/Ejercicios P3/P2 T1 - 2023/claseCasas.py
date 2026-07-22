from claseInmuebles import Inmueble


class Casa(Inmueble):
    __mtsCuadrados: float

    def __init__(self, localidad, direccion, superficie, mtsCuadrados):
        super().__init__(localidad, direccion, superficie)
        self.__mtsCuadrados = mtsCuadrados

    def getMetrosCuadrados(self):
        return self.__mtsCuadrados

    def importeDeVenta(self):
        precioConst = self.__mtsCuadrados * 1.80 * 20000
        total = self.getSuperficie() * 15 * precioConst
        return total

    def __str__(self):
        return f"Metros cuadrados del terreno: {self.__mtsCuadrados} | \nImporte de venta: {self.importeDeVenta()}"
