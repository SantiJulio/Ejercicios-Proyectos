class Inscripcion:
    __dniA: int
    __id: int
    __descripcion: str
    __fecha: str
    __estado: str
    __arancel: int
    __porcentaje: int

    def __init__(self,dniA,id,descripcion,fecha,estado,arancel,porcentaje):
        self.__dniA = dniA
        self.__id = id
        self.__descripcion = descripcion
        self.__fecha = fecha
        self.__estado = estado
        self.__arancel = arancel
        self.__porcentaje = porcentaje

    def getDniA(self):
        return self.__dniA

    def getId(self):
        return self.__id

    def getDescripcion(self):
        return self.__descripcion

    def getFecha(self):
        return self.__fecha

    def getEstado(self):
        return self.__estado

    def getArancel(self):
        return self.__arancel

    def getPorcentaje(self):
        return self.__porcentaje

    def __str__(self):
        return (f"""
                 Dni Aspirante {self.__dniA}
                 Identificador {self.__id}
                 Descripcion {self.__descripcion}
                 Fecha {self.__fecha}
                 Estado {self.__estado}
                 Arancel {self.__arancel}
                 Porcentaje {self.__porcentaje}
                 """)   
    
    def __eq__(self, otro):
        if not isinstance(otro, Inscripcion):
            return False
        return(self.__dniA == otro.getDniA() and
               self.__id == otro.getId() and
               self.__descripcion == otro.getDescripcion())