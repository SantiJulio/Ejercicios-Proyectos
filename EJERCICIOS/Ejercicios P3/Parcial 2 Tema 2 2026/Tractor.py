from Maquina import Maquina

class Tractor(Maquina):
    __potencia: float
    __tipoT: str
    
    def __init__(self,potencia,tipoT,id,marca,modelo,anio,precio):
        super().__init__(id,marca,modelo,anio,precio)
        self.__potencia = potencia
        self.__tipoT = tipoT

    def getPotencia(self):
        return self.__potencia

    def getTipoT(self):
        return self.__tipoT

    def calculoSubTotal(self):
        subtotal = self.getPrecio() + (1500 * (self.getPotencia() / 10))
        if self.__tipoT == 'Doble':
            subDoble = subtotal + 8000
        else: 
            subDoble = subtotal    
        return subDoble 

    def mostrarDatos(self):
        print(f"Id: {self.getId()}, Modelo: {self.getModelo()}, ImporteF: {self.ImporteFinal()}")   