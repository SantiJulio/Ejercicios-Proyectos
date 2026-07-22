from Espectaculo import Espectaculo

class Concierto(Espectaculo):
    __banOart: str
    __cantM: int

    def __init__(self,ba,cant,nombre,fecha,precio):
        super().__init__(nombre,fecha,precio)
        self.__banOart = ba
        self.__cantM = cant

    def getBanOArt(self):
        return self.__banOart

    def getCantM(self):
        return self.__cantM

    def __str__(self):
        return(f"{super().__str__()}, Banda o Artista: {self.__banOart}, CantM: {self.__cantM}")

    def precioEntrada(self):
        porMus = self.getCantM() * 500
        return self.getPrecio() + porMus    
    
    def mostrarDatos(self):
        print(f"""
                Nombre: {self.getNombre()}
                Fecha: {self.getFecha()}
                Precio Final: {self.precioEntrada()}
                """)