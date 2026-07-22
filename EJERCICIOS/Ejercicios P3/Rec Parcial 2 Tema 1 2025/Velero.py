from Embarcacion import Embarcacion

class Velero(Embarcacion):
    __cantV: int
    __costoD = 200000

    def __init__(self,cantV,nom,esl,anio,costo,dispo,cantD):
        super().__init__(nom,esl,anio,costo,dispo,cantD)
        self.__cantV = cantV

    @classmethod
    def getCostoD(cls):
        return cls.__costoD

    def getCantV(self):
        return self.__cantV

    def __str__(self):
        return (f"{super().__str__()}, Cantidad velas: {self.__cantV}")
    
    def costoTotal(self):
        base = Velero.getCostoD()
        porVela = 20000 * self.getCantV()
        return (base + porVela) * self.getCantD()
    
    def mostrarAlquilado(self):
        print(f"""
               Nombre: {self.getNomE()} 
               Costo Total: {self.costoTotal()}
               """)