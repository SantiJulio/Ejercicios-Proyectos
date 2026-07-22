from Espectaculo import Espectaculo

class Obra(Espectaculo):
    __nomD: str
    __duracion: int

    def __init__(self,nomD,duracion,nombre,fecha,precio):
        super().__init__(nombre,fecha,precio)
        self.__nomD = nomD
        self.__duracion = duracion

    def getNomD(self):
        return self.__nomD

    def getDuracion(self):
        return self.__duracion

    def __str__(self):
        return(f"{super().__str__()}, NomD: {self.__nomD}, Duracion: {self.__duracion}")

    def precioEntrada(self):
        base = self.getPrecio()
        porMin = self.getDuracion() * 10
        return base + porMin    
    
    def mostrarDatos(self):
        print(f"""
                Nombre: {self.getNombre()}
                Fecha: {self.getFecha()}
                Precio Final: {self.precioEntrada()}
                """)