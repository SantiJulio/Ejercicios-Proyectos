class MaterialPrestado:
    __dniS: int
    __id: str
    __descripcion: str
    __fechaP: str
    __estado: str
    __fechaD: str
    __garantia: int
    
    def __init__(self,dniS,id,descripcion,fechaP,estado,fechaD,garantia):
        self.__dniS = dniS
        self.__id = id
        self.__descripcion = descripcion
        self.__fechaP = fechaP
        self.__estado = estado
        self.__fechaD = fechaD
        self.__garantia = garantia

    def getDniS(self):
        return self.__dniS

    def getId(self):
        return self.__id

    def getDescripcion(self):
        return self.__descripcion
    
    def getFechaP(self):
        return self.__fechaP
    
    def getEstado(self):
        return self.__estado

    def getFechaD(self):
        return self.__fechaD

    def getGarantia(self):
        return self.__garantia
    
    def __str__(self):
        return f"""
                Dni Solicitante {self.__dniS}
                Identificador {self.__id}
                Descripcion {self.__descripcion}
                Fecha Prestamo {self.__fechaP}
                Estado {self.__estado}
                Fecha Devolucion {self.__fechaD}
                Garantia {self.__garantia}
                """
    
    def setEstado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def setFechaD(self, nuevo_fechaD):
        self.__fechaD = nuevo_fechaD

    def __eq__(self,otro):
        if not isinstance(otro,MaterialPrestado):
            return False
        return (self.__id == otro.getId() and
                self.__descripcion == otro.getDescripcion() and
                self.__dniS == otro.getDniS())        