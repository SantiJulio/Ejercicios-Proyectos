class Invitado:
    __id: int
    __nomI: str
    __dni: int
    __email: str
    __dir: str

    def __init__(self,id,nomI,dni,email,dir):
        self.__id = id
        self.__nomI = nomI
        self.__dni = dni
        self.__email = email
        self.__dir = dir

    def getId(self):
        return self.__id

    def getNomI(self):
        return self.__nomI

    def getDni(self):
        return self.__dni

    def getEmail(self):
        return self.__email

    def getDir(self):
        return self.__dir

    def __str__(self):
        return(f"""
                ID: {self.__id}
                NomI: {self.__nomI}
                DNI: {self.__dni}
                Email: {self.__email}
                Dir: {self.__dir}
                """)         