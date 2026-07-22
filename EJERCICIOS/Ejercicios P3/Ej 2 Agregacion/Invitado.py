class Invitado:
    __idE: int
    __nombreI: str
    __dni: int
    __email: str
    __direccion: str

    def __init__(self,idE,nombreI,dni,email,direccion):
        self.__idE = idE
        self.__nombreI = nombreI
        self.__dni = dni
        self.__email = email
        self.__direccion = direccion

    def getIdE(self):
        return self.__idE
    
    def getNombreI(self):
        return self.__nombreI
    
    def getDni(self):
        return self.__dni
    
    def __str__(self):
        return(f"""
                IdE {self.__idE}
                NombreI {self.__nombreI}
                DNI {self.__dni}
                """)