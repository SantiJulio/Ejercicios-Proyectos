class Hospital:
    __cod: int
    __nom: str
    __dir: str
    __loc: str
    __tel: str

    def __init__(self,cod,nom,dir,loc,tel):
        self.__cod = cod
        self.__nom = nom
        self.__dir = dir
        self.__loc = loc
        self.__tel = tel

    def getCodigo(self):
        return self.__cod
    
    def getNombre(self):
        return self.__nom
    
    def getDireccion(self):
        return self.__dir
    
    def getLocalidad(self):
        return self.__loc
    
    def getTelefono(self):
        return self.__tel
    
    def __str__(self):
        return f"""
                Hospital {self.__nom}
                Codigo {self.__cod}
                Direccion {self.__dir}
                Localidad {self.__loc}
                Telefono {self.__tel}
                """