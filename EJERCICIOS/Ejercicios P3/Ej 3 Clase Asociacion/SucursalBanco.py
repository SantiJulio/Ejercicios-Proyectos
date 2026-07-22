class SucursalBanco:
    __id: int
    __denominacion: str
    __domicilio: str
    __telefono: str
    __departamento: str
    __listaCS: list

    def __init__(self,id,denominacion,domicilio,telefono,departamento):
        self.__id = id
        self.__denominacion = denominacion
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__departamento = departamento
        self.__listaCS = []