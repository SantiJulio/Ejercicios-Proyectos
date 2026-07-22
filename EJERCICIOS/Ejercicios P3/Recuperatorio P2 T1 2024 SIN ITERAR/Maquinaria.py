from Equipo import Equipo

class Maquinaria(Equipo):
    __tipoM: str
    __peso: int

    def __init__(self,tipoM,peso,marca,modelo,anioF,tipoC,potencia,capac,tarifa,cantD):
        super().__init__(marca,modelo,anioF,tipoC,potencia,capac,tarifa,cantD)
        self.__tipoM = tipoM
        self.__peso = peso

    def getTipoM(self):
        return self.__tipoM

    def getPeso(self):
        return self.__peso

    def calcular(self):
        if self.__peso <= 10:
            valor = super().calcular()
        else:          
            valor = super().calcular()
            valor = valor + (valor * (20 / 100))
        return valor 

    def __str__(self):
        return(f"{super().__init__()}, Tipo Maquina: {self.__tipoM}, Peso: {self.__peso}")   