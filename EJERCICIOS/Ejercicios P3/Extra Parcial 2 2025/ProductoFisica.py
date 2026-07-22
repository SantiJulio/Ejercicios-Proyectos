from Producto import Producto

class ProductoFisica(Producto):
    __dir: str
    __tasa: int

    def __init__(self,dir,tasa,cod,nom,pre,des,sto):
        super().__init__(cod,nom,pre,des,sto)
        self.__dir = dir
        self.__tasa = tasa

    def getDir(self):
        return self.__dir

    def getTasa(self):
        return self.__tasa

    def __str__(self):
        return(f"{super().__str__()}, Direccion: {self.__dir}, Tasa de Impuesto: {self.__tasa}")    
    
    def precioFinal(self):
        impuesto = self.getPrecio() *(self.getTasa() / 100)
        return self.getPrecio + impuesto 
    
    def mostrar(self):
        print(f"Nombre: {self.getNombre()}, Tipo: {self.getTipo()}, Precio Total: {self.precioFinal()}")