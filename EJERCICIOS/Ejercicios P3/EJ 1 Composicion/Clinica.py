from Consultorio import Consultorio

class Clinica:
    __id: int
    __nombre: str
    __direccion: str
    __director: str
    __cantP: int
    __listaC: list

    def __init__(self,id,nombre,direccion,director,cantP):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__director = director
        self.__cantP = cantP
        self.__listaC = []

    def agregarConsultorio(self,idC,nroC,piso,espec,costo,estado):
        unConsultorio = Consultorio(idC,nroC,piso,espec,costo,estado)
        self.__listaC.append(unConsultorio)

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getCantP(self):
        return self.__cantP
    
    def getListaC(self):
        return self.__listaC

    def __str__(self):
        return (f"""
                Identificador {self.__id}
                Nombre {self.__nombre}
                Cantidad de pisos {self.__cantP}
                Lista {self.__listaC}
                """)  

    def buscarPorNroYEstado(self, nro, estado):
        cli = 0
        encontrado = False
        while cli < self.__listaC and not encontrado:
            if cli.getNroC() == nro and cli.getEstado() == estado:
                encontrado = True
                return cli
            else: 
                i += 1         

    def registrarNroC(self, nroC):
        cli = self.buscarPorNroYEstado(nroC, "Libre")
        if cli:
            cli.setEstado("Ocupado")
            return True
        return False

    def liberarNroC(self, nro):
        cli = self.buscarPorNroYEstado(nro, "Ocupado")       
        if cli:
            cli.setEstado("Libre")
            return True
        return False

    """def registrarNroC(self,nroC):
        registrado = False
        for cli in self.__listaC:
            if not registrado and cli.getNroC() == nroC and cli.getEstado().lower() == "Libre":
                cli.ocupado()
                registrado = True
        return registrado  

    def liberarNroC(self,nro):
        liberado = False
        for cli in self.__listaC:
            if not liberado and cli.getNroC() == nro and cli.getEstado().lower() == "Ocupado":
                cli.libre()
                liberado = True
        return liberado"""             