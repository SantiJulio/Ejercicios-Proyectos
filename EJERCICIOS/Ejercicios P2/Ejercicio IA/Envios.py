class Envio:
    __barrioOr: str
    __barrioDes: str
    __tiempo : int
    __idDr = str

    def __init__(self,barrrioO,barrioD,ti,idD):
        self.__barrioOr = barrrioO
        self.__barrioDes = barrioD
        self.__tiempo = ti
        self.__idDr = idD

    def getBarrioOr(self):
        return self.__barrioOr
    
    def getBarrioDes(self):
        return self.__barrioDes
    
    def getTiempo(self):
        return self.__tiempo
    
    def getIdDr(self):
        return self.__idDr
    
    def __str__(self):
        return(f"""
                Barrio Origen {self.__barrioOr}
                Barrio Destino {self.__barrioDes}
                Tiempo {self.__tiempo}
                ID Dron {self.__idDr}
                """)
    
    def __gt__(self,otro):
        return self.__tiempo > otro.getTiempo()