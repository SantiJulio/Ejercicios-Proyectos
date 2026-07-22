

class Invitado:
    __nombre: str
    __dni: int
    __email: str
    __direccion: str

    def __init__(self, nombre, dni, email, dir):
        self.__nombre = nombre
        self.__dni = int(dni)
        self.__email = email
        self.__direccion = dir

    def __str__(self):
        return f"Nombre: {self.__nombre} - DNI: {self.__dni}"

    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_email(self):
        return self.__email
    
    def get_direccion(self):
        return self.__direccion