class Solicitante:
    __dni: int
    __nya: str
    __direccion: str
    __telefono: int
    
    def __init__(self,dni,nya,direccion,telefono):
        self.__dni = dni
        self.__nya = nya
        self.__direccion = direccion
        self.__telefono = telefono

    def getDni(self):
        return self.__dni
    
    def getNyA(self):
        return self.__nya
    
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f"""
                DNI {self.__dni}
                Nombre y Apellido {self.__nya}
                Telefono {self.__telefono}
                """    