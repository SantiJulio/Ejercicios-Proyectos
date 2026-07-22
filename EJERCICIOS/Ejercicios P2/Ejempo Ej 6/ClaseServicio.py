class Servicio:
    __codigo: int
    __nombre: str
    __especialidad: str
    __horario: str
    __codigoHospital: int
    def __init__(self, codigo, nombre, especialidad, horario, codigoHospital):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__horario = horario
        self.__codigoHospital = codigoHospital
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getEspecialidad(self):
        return self.__especialidad
    def getHorario(self):
        return self.__horario
    def getCodHospital(self):
        return self.__codigoHospital
    def __str__(self):
        return f"""
                Servicio {self.__nombre}
                Codigo {self.__codigo}
                Especialidad {self.__especialidad}
                Horario {self.__horario}
                Hospital que tiene el servicio {self.__codigoHospital}
                """
    def __gt__(self, otro):
        return self.getNombre() > otro.getNombre()
    def __lt__(self, otro):
        return self.getNombre() < otro. getNombre()