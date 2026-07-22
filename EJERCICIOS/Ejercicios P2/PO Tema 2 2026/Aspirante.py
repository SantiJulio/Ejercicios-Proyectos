class Aspirante:
    __dni: int
    __nombre: str
    __apellido: str
    __direccion: str
    __departamento: str
    __telefono: int

    def __init__(self,dni,nombre,apellido,direccion,departamento,telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__departamento = departamento
        self.__telefono = telefono

    def getDni(self):
        return self.__dni 

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def __str__(self):
        return(f"""
                DNI {self.__dni}
                Nombre {self.__nombre}
                Apellido {self.__apellido}
                Telefono {self.__telefono}
                """)        