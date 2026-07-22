from claseInmuebles import Inmueble

class Departamento(Inmueble):
    __cantDormitorios: int
    __numMonoblock: int
    __numDpto: int
    __piso: int

    def __init__(
        self,
        localidad,
        direccion,
        superficie,
        cantDormitorios,
        numMonoblock,
        numDpto,
        piso,
    ):
        super().__init__(localidad, direccion, superficie)
        self.__cantDormitorios = cantDormitorios
        self.__numMonoblock = numMonoblock
        self.__numDpto = numDpto
        self.__piso = piso

    def getCantidadDormitorios(self):
        return self.__cantDormitorios

    def getNumeroMonoblock(self):
        return self.__numMonoblock

    def getNumeroDepto(self):
        return self.__numDpto

    def getPiso(self):
        return self.__piso

    def importeDeVenta(self):
        precioDeConst = self.__cantDormitorios * 17000
        total = self.getSuperficie() * 15 * precioDeConst
        return total

    def __str__(self):
        return f"Cantidad de dormitorios: {self.__cantDormitorios} | \nNumero de Monoblock: {self.__numMonoblock} | \nNumero de Dpto: {self.__numDpto} | \nPiso: {self.__piso} | \nImporte de venta: {self.importeDeVenta()}"
