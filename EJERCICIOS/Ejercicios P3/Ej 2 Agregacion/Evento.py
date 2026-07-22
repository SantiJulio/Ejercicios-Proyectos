class Evento:
    __id: int
    __nombreE: str
    __fecha: str
    __tipo: str
    __listaI: list

    def __init__(self,id,nombreE,fecha,tipo):
        self.__id = id
        self.__nombreE = nombreE
        self.__fecha = fecha
        self.__tipo = tipo
        self.__listaI = []

    def getId(self):
        return self.__id

    def getNombreE(self):
        return self.__nombreE

    def getFecha(self):
        return self.__fecha

    def getTipo(self):
        return self.__tipo
    
    def getListaI(self):
        return self.__listaI
    
    def agregarInvitado(self,unInvitado):
        self.__listaI.append(unInvitado)

    def __str__(self):
        return(f"""
                ID {self.__id}
                NombreE {self.__nombreE}
                Fecha {self.__fecha}
                Tipo {self.__tipo}
                """)    