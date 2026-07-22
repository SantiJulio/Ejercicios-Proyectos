class Disertante:
    __nombre: str
    __especialidad: str
    __universidad: str

    def __init__(self,nom,esp,uni):
        self.__nombre = nom
        self.__especialidad = esp
        self.__universidad = uni

    def getNombre(self):
        return self.__nombre

    def getEspecialidad(self):
        return self.__especialidad

    def getUniversidad(self):
        return self.__universidad

    def __str__(self):
        return(f"""
                Nombre {self.__nombre}
                Especialidad {self.__especialidad}
                Universidad {self.__universidad}
                """)    