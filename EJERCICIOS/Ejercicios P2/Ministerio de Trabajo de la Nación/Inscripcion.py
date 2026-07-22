class Inscripcion:
    __idCurso: int
    __apellido: str
    __nombre: str
    __dni: int
    __provinciaP: str
    __estado: str

    def __init__(self,idCurso,apellido,nombre,dni,provinciaP,estado):
        self.__idCurso = idCurso
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__provinciaP = provinciaP
        self.__estado = estado

    def getIdCurso(self):
        return self.__idCurso
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni
    
    def getProvinciaP(self):
        return self.__provinciaP

    def getEstado(self):
        return self.__estado

    def __str__(self):
        return f"""
                Id Curso {self.__idCurso}
                Apellido {self.__apellido}
                Nombre {self.__nombre}
                Dni {self.__dni}
                Provincia Persona {self.__provinciaP}
                Estado {self.__estado}
                """
    
    def setEstado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def __eq__(self,otro):
        if not isinstance(otro, Inscripcion):
            return False
        return (self.__dni == otro.getDni() and
                self.__apellido == otro.getApellido() and
                self.__nombre == otro.getNombre() and
                self.__provinciaP == otro.getProvinciaP())    

    def __lt__(self,otro):
        if self.__apellido.lower() == otro.getApellido().lower():
            return self.__nombre.lower() < otro.getNombre().lower()
        return self.__apellido.lower() < otro.getApellido().lower()