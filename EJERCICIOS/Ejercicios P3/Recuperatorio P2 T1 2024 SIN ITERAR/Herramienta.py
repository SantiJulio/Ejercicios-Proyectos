from Equipo import Equipo

class Herramienta(Equipo):
    __tipoH: str

    def __init__(self,tipoH,marca,modelo,anioF,tipoC,potencia,capac,tarifa,cantD):
        super().__init__(marca,modelo,anioF,tipoC,potencia,capac,tarifa,cantD)
        self.__tipoH = tipoH

    def getTipoH(self):
        return self.__tipoH

    def calcular(self):
        if self.__tipoH == 'Bateria':
            valor = super().tarifaAlquiler()
        elif self.__tipoH == 'Cable':
            valor = super().tarifaAlquiler()
            valor = valor + (valor * (10 / 100))  
        return valor                   
    
    def __str__(self):
        return(f"{super().__init__()}, Tipo Herramienta: {self.__tipoM}")