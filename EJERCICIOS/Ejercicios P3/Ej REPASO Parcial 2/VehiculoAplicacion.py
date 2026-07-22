from Vehiculo import Vehiculo

class VehiculoAplicacion(Vehiculo):
    __url: str
    __porcD: int
    __seguro: bool
    __costo: float

    def __init__(self,url,porcD,seguro,costo,cod,marca,modelo,precio,cantD):
        super().__init__(cod,marca,modelo,precio,cantD)
        self.__url = url
        self.__porcD = porcD
        self.__seguro = seguro
        self.__costo = costo

    def getUrl(self):
        return self.__url

    def getPorcD(self):
        return self.__porcD

    def getSeguro(self):
        return self.__seguro

    def getCosto(self):
        return self.__costo

    def __str__(self):
        return(f"""
                {super().__str__()}
                URL: {self.__url}
                PorcD: {self.__porcD}
                Seguro: {self.__seguro}
                """)

    def costoFinal(self):
        descuento = self.getPrecio() * (self.getPorcD / 100)
        if self.__seguro:
            costoF = self.getPrecio() + self.getSeguro() - descuento
        else:
            costoF = self.getPrecio() - descuento

    def mostrar(self):
        print(f"Marca: {self.getMarca()}, Modelo: {self.getModelo}, Tipo: {self.getTipo()}, Costo Final: {self.costoFinal()}")                     