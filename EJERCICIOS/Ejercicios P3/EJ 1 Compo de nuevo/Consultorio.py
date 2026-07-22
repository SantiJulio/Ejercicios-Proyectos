class Consultorio:
    __idC: int
    __nroC: int
    __piso: int
    __esp: str
    __costo: float
    __estado: str

    def __init__(self,idC,nroC,piso,esp,costo,estado):
        self.__idC = idC
        self.__nroC = nroC
        self.__esp = esp
        self.__costo = costo
        self.__estado = estado

    def getIdC(self):
        return self.__idC

    def getNroC(self):
        return self.__nroC
    
    def getPiso(self):
        return self.__piso
    
    def getEsp(self):
        return self.__esp
    
    def getCosto(self):
        return self.__costo
    
    def getEstado(self):
        return self.__estado
    
    def __str__(self):
        return(f"""
                IDC: {self.__idC}
                NroC: {self.__nroC}
                Esp: {self.__esp}
                Costo: {self.__costo}
                Estado: {self.__estado}
                """)
    
    def setEstado(self, nuevoEstado):
        self.__estado = nuevoEstado

    def __lt__(self,otro):
        if self.__piso != otro.getPiso():
            return self.__piso < otro.getPiso()
        return self.__nroC < otro.getNroC()      