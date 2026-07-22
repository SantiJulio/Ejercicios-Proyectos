class Estudiante:
    __nombre: str
    __apellido: str
    __dni: int
    __correo: str
    __ciudadR: str

    def __init__(self,nombre,apellido,dni,correo,ciudadR):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__correo = correo
        self.__ciudadR = ciudadR

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def __str__(self):
        return(f"""
                Nombre: {self.__nombre}
                Apellido: {self.__apellido}
                Dni: {self.__dni}
                Correo: {self.__correo}
                CiudadR: {self.__ciudadR}    
                """) 