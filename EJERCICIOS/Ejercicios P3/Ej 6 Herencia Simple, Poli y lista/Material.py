class Material:
    __nombreM: str
    __cantM: int
    __costo: int

    def __init__(self,nom,cant,cos):
        self.__nombreM = nom
        self.__cantM = cant
        self.__costo = cos

    def getNombreM(self):
        return self.__nombreM

    def getCantM(self):
        return self.__cantM 

    def getCosto(self):
        return self.__costo

    def __str__(self):
        return(f"""
                Nombre Material {self.__nombreM}
                Cantidad Material {self.__cantM}
                Costo {self.__costo}
                """)   