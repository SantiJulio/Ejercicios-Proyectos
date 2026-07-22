from Embarcacion import Embarcacion

class Lancha(Embarcacion):
    __potencia: float
    __costoD: 300000

    def __init__(self,potencia,nom,esl,anio,costo,dispo,cantD):
        super().__init__(nom,esl,anio,costo,dispo,cantD)
        self.__potencia = potencia

    @classmethod
    def getCostoD(cls):
        return cls.__costoD

    def getPotencia(self):
        return self.__potencia

    def __str__(self):
        return(f"{super().__str__()}, Potencia: {self.__potencia}")    
    
    def costoTotal(self):
        base = Lancha.getCostoD()
        porHp = 5000 * self.getPotencia()
        return (base + porHp) * self.getCantD()
    
    def mostrarAlquilado(self):
        print(f"""
               Nombre: {self.getNomE()} 
               Costo Total: {self.costoTotal()}
               """)