from Invitado import Invitado

class Evento:
    __idE: int
    __nomE: str
    __fecha: str
    __tipo: str
    __listaI: list

    def __init__(self,idE,nomE,fecha,tipo):
        self.__idE = idE
        self.__nomE = nomE
        self.__fecha = fecha
        self.__tipo = tipo
        self.__listaI = []

    def agregarInvitado(self,unInvitado):
        self.__listaI.append(unInvitado)

    def getIdE(self):
        return self.__idE

    def getNomE(self):
        return self.__nomE

    def getFecha(self):
        return self.__fecha

    def getTipo(self):
        return self.__tipo

    def getListaI(self):
        return self.__listaI

    def __str__(self):
        return(f"""
                IdE: {self.__idE}
                NomE: {self.__nomE}
                Fecha: {self.__fecha}
                Tipo: {self.__tipo}
                """) 

    def mostrarInvi(self,xid):
        for i in range(len(self.__listaI)):
            if self.__listaI[i].getId() == xid:
                print(f"Nombre Invitado: {self.__listaI[i].getNomI()}")               

    def mostrarRegistrado(self,xdni):
        i = 0
        encontrado = False
        while i < len(self.__listaI) and not encontrado:
            if self.__listaI[i].getDni() == xdni:
                encontrado = True
            else:
                i += 1
        return encontrado                            