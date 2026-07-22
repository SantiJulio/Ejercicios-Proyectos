from Vehiculo import Vehiculo

class VehiculoSucursal(Vehiculo):
    __dir: str
    __porcR: int

    def __init__(self,dir,porcR,cod,marca,modelo,precio,cantD):
        super().__init__(cod,marca,modelo,precio,cantD)
        self.__dir = dir
        self.__porcR = porcR

    def getDir(self):
        return self.__dir

    def getPorcR(self):
        return self.__porcR

    def __str__(self):
        return(f"""
                {super().__str__()}
                Direccion: {self.__dir}
                Porcentaje Recargo: {self.__porcR}
                """)

    def costoFinal(self):
        recargo = self.getPrecio() * (self.getPorcR() / 100)
        return self.getPrecio() + recargo        
    
    def mostrar(self):
        print(f"Marca: {self.getMarca()}, Modelo: {self.getModelo}, Tipo: {self.getTipo()}, Costo Final: {self.costoFinal()}")