from Producto import Producto

class ProductoLinea(Producto):
    __url:str
    __porcD: int
    __envio: bool
    __costoE: int

    def __init__(self,url,porcD,envio,costoE,cod,nom,pre,des,sto):
        super().__init__(cod,nom,pre,des,sto)
        self.__url = url
        self.__porcD = porcD
        self.__envio = envio
        self.__costoE = costoE

    def getUrl(self):
        return self.__url

    def getPorcD(self):
        return self.__porcD 

    def getEnvio(self):
        return self.__envio

    def getCostoE(self):
        return self.__costoE

    def __str__(self):
        return(f"{super().__str__()}, URL: {self.__url}, PorcD: {self.__porcD}, Envio: {self.__envio}, CostoE: {self.__costoE}")

    def precioFinal(self):
        descuento = self.getPrecio() * (self.getPorcD() / 100)
        if self.__envio:
            precioFinal = self.getPrecio() - descuento
        else:
            precioFinal = self.getPrecio() + self.getCostoE()
        return precioFinal       

    def mostrar(self):
        print(f"Nombre: {self.getNombre()}, Tipo: {self.getTipo()}, Precio Total: {self.precioFinal()}")