class Fraccion:
    __numerador: int
    __denominador: int

    def __init__(self,numerador,denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    def __str__(self):
        return "{}/{}".format(self.__numerador, self.__denominador)

    def get_Numerador(self):
        return self.__numerador

    def get_Denominador(self):
        return self.__denominador
    
        