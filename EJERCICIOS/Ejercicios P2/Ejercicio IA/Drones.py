class Dron:
    __idDron = str
    __marca = str
    __modelo = str
    __batMax = int
    __dniOper = str
    __consumoProm = 150

    def __init__(self,idDr,mar,mod,batM,dni):
        self.__idDron = idDr
        self.__marca = mar
        self.__modelo = mod
        self.__batMax = batM
        self.__dniOper = dni

    @classmethod
    def getConsumo(cls):
        return cls.__consumoProm

    def getIdDron(self):
        return self.__idDron

    def getDniO(self):
        return self.__dniOper
    
    def __str__(self):
        return(f"""
                Id Dron {self.__idDron}
                Dni Oper {self.__dniOper}
                """)
    