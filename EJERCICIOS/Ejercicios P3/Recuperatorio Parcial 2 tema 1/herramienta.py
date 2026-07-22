from equipos import Equipo

class Herramienta(Equipo):
    __tipoH: str

    def __init__(self, marca, mod, anio, tipoC, pot, cap, tarifa, dias, tipo):
        super().__init__(marca, mod, anio, tipoC, pot, cap, tarifa, dias)
        self.__tipoH = tipo
    
    def getTipo(self):
        return self.__tipoH
    
    def calcularTarifa(self):
        if self.__tipoH == 'Cable':
            valor = super().calcular()    
        elif self.__tipoH == 'Bateria':
            valor = super().calcular()
            valor += valor * 0.10
        
        return valor
    
    def __str__(self):
        return super().__str__() + f"Tipo: {self.__tipoH}"
    