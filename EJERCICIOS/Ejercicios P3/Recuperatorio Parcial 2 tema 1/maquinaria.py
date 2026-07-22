from equipos import Equipo

class Maquinaria(Equipo):
    __tipoM: str
    __peso: int

    def __init__(self, marca, mod, anio, tipoC, pot, cap, tarifa, dias, tipo, peso):
        super().__init__(marca, mod, anio, tipoC, pot, cap, tarifa, dias)
        self.__tipoM = tipo
        self.__peso = peso

    def getTipoM(self):
        return self.__tipoM
    def getPeso(self):
        return self.__peso
    
    def calcularTarifa(self):
        if self.__peso <= 10:
            valor = super().calcular()
        elif self.__peso > 10:
            valor = super().calcular()
            valor += valor * 0.20
        return valor
    
    def __str__(self):
        return super().__str__() + f"Tipo: {self.__tipoM} - Peso: {self.__peso}"
    