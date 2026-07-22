class Consultorio:
    __idC: int
    __nroC: int
    __piso: int
    __especialidad: str
    __costo: float
    __estado: str

    def __init__(self,idC,nroC,piso,especialidad,costo,estado):
        self.__idC = idC
        self.__nroC = nroC
        self.__piso = piso
        self.__especialidad = especialidad
        self.__costo = costo
        self.__estado = estado

    def getIdC(self):
        return self.__idC

    def getNroC(self):
        return self.__nroC

    def getPiso(self):
        return self.__piso

    def getEspecialidad(self):
        return self.__especialidad

    def getCosto(self):
        return self.__costo

    def getEstado(self):
        return self.__estado    
    
    def __str__(self):
        return (f"""
                 Identificador {self.__idC}
                 Numero Consultorio {self.__nroC}
                 Numero Piso {self.__piso}
                 Especialidad {self.__especialidad}
                 Costo Diario {self.__costo}
                 Estadio {self.__estado}
                 """)
    
    def setEstado(self, nuevoEstado):
        self.__estado = nuevoEstado

    def __lt__(self,otro):
        if self.__piso != otro.getPiso():
            return self.__piso < otro.getPiso()
        return self.__nroC < otro.getNroC()