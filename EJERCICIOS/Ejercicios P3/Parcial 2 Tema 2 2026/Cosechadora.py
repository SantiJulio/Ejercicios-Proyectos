from Maquina import Maquina

class Cosechadora(Maquina):
    __capac: int
    __tipoC: str

    def __init__(self,capac,tipoC,id,marca,modelo,anio,precio):
        super().__init__(id,marca,modelo,anio,precio)
        self.__capac = capac
        self.__tipoC = tipoC

    def getCapac(self):
        return self.__capac

    def getTipoC(self):
        return self.__tipoC   

    def calculoSubTotal(self): 
        if self.__tipoC == 'Maicero':
            subtotal = (self.getPrecio() + (self.getPrecio() * (15 / 100))) + (10 * self.getCapac())
        else: 
            subtotal = self.getPrecio() + (10 * self.getCapac())
        return subtotal 
    
    def mostrarDatos(self):
        print(f"Id: {self.getId()}, Modelo: {self.getModelo()}, ImporteF: {self.ImporteFinal()}")