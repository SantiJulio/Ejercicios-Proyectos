from Ingrediente import Ingrediente

class Receta:
    __idR: int
    __nomR: str
    __cat: str
    __listaI: list

    def __init__(self,idR,nomR,cat):
        self.__idR = idR
        self.__nomR = nomR
        self.__cat = cat
        self.__listaI = []

    def agregarIngrediente(self,id,nomI,unidad,stock):
        unIngrediente = Ingrediente(id,nomI,unidad,stock)
        self.__listaI.append(unIngrediente)

    def getIdR(self):
        return self.__idR

    def getNomR(self):
        return self.__nomR

    def getCat(self):
        return self.__cat
    
    def getLista(self):
        return self.__listaI

    def __str__(self):
        return(f"""
                IdR: {self.__idR}
                NomR: {self.__nomR}
                Cat: {self.__cat}
                """)  

    def mostrarPorNom(self,xnomI):
        i = 0
        encontrado = False
        while i < len(self.__listaI) and not encontrado:
            if self.__listaI[i].getNomI() == xnomI:
                encontrado = True
            else:
                i += 1
        return encontrado
