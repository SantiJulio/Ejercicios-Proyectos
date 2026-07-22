class Servicio:
    __codS: int
    __nomS: str
    __esp: str
    __horaA: str
    __codH: int

    def __init__(self,codS,nomS,esp,horaA,codH):
        self.__codS = codS
        self.__nomS = nomS
        self.__esp = esp
        self.__horaA = horaA
        self.__codH = codH

    def getCodigo(self):
        return self.__codS

    def getNombre(self):
        return self.__nomS

    def getEspecialidad(self):
        return self.__esp

    def getHora(self):
        return self.__horaA

    def getCodigoH(self):
        return self.__codH

    def __str__(self):
        return f"""
                Servicio {self.__nomS}
                Codigo {self.__codS}
                Especialidad {self.__esp}
                Horario {self.__horaA}
                Hospital que tiene el servicio {self.__codH}
                """