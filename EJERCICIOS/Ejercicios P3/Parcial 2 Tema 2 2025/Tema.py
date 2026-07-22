class Tema:
    __codM: str
    __nomT: str
    __desc: str

    def __init__(self,codM,nomT,desc):
        self.__codM = codM
        self.__nomT = nomT
        self.__desc = desc

    def getCodM(self):
        return self.__codM

    def getNomT(self):
        return self.__nomT 

    def getDesc(self):
        return self.__desc

    def __str__(self):
        return(f"""
                CodM: {self.__codM}
                NomT: {self.__nomT}
                Desc: {self.__desc}
                """)   