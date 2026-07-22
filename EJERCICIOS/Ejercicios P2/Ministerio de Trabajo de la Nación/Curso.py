class Curso:
    __idC: int
    __denominacion: str
    __cantH: int
    __provincia: str
    __cupoI: int
    __cupoA: int

    def __init__(self,idC,denominacion,cantH,provincia,cupoI,cupoA):
        self.__idC = idC
        self.__denominacion = denominacion
        self.__cantH = cantH
        self.__provincia = provincia
        self.__cupoI = cupoI
        self.__cupoA = 0

    def getIdC(self):
        return self.__idC

    def getDenominacion(self):
        return self.__denominacion

    def getCantH(self):
        return self.__cantH

    def getCupoI(self):
        return self.__cupoI

    def getCupoA(self):
        return self.__cupoA

    def __str__(self):
        return f"""
                Identificador {self.__idC}
                Denominacion {self.__denominacion}
                Cantidad Horas {self.__cantH}
                Cupo Inscriptos {self.__cupoI}
                Cupo Aceptado {self.__cupoA}
                """
    
    def actualizarCupoA(self):
        self.__cupoA += 1