class Ingrediente:
    __id: int
    __nomI: str
    __unidad: str
    __stock: int

    def __init__(self,id,nomI,unidad,stock):
        self.__id = id
        self.__nomI = nomI
        self.__unidad = unidad
        self.__stock = stock

    def getId(self):
        return self.__id

    def getNomI(self):
        return self.__nomI

    def getUnidad(self):
        return self.__unidad

    def getStock(self):
        return self.__stock 

    def __str__(self):
        return(f"""
                ID: {self.__id}
                NomI: {self.__nomI}
                Unidad: {self.__unidad}
                Stock: {self.__stock}
                """)     
    
    