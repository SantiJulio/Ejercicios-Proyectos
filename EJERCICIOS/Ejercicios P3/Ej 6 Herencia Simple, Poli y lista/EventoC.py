class EventoC:
    __codigo: str
    __titulo: str
    __institucion: str
    __fecha: str
    __cantMA: int

    def __init__(self,cod,tit,inst,fecha,cant):
        self.__codigo = cod
        self.__titulo = tit
        self.__institucion = inst
        self.__fecha = fecha
        self.__cantMA = cant

    def getCodigo(self):
        return self.__codigo
    
    def getTitulo(self):
        return self.__titulo
    
    def getInstitucion(self):
        return self.__institucion
    
    def getFecha(self):
        return self.__fecha
    
    def getCantMA(self):
        return self.__cantMA
    
    def __str__(self):
        return(f"""
                Codigo {self.__codigo}
                Titulo {self.__titulo}
                Institucion {self.__institucion}
                Fecha {self.__fecha}
                CantMA {self.__cantMA}
                """)