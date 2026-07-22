from Cabaña import Cabaña

class Complejo: 
    __id: str
    __nombre: str
    __ubi: str
    __encargado: str
    __cantEst: int
    __listaCabañas: list

    def __init__(self,id,nombre,ubi,encargado,cantEst):
        self.__id = id
        self.__nombre = nombre
        self.__ubi = ubi
        self.__encargado = encargado
        self.__cantEst = cantEst
        self.__listaCabañas = []

    def agregarCabaña(self,nro,planta,cantD,costo,estado):
        unaCabaña = Cabaña(nro,planta,cantD,costo,estado) 
        self.__listaCabañas.append(unaCabaña)   

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre 
    
    def getUbi(self):
        return self.__ubi
    
    def getEncargado(self):
        return self.__encargado
    
    def getCantEst(self):
        return self.__cantEst
    
    def getListaCabañas(self):
        return self.__listaCabañas
    
    def __str__(self):
        return(f"""
                Id: {self.__id}
                Nombre: {self.__nombre}
                Ubi: {self.__ubi}
                Encargado: {self.__encargado}
                CantEst: {self.__cantEst}
                """)
    
    def buscarP(self,xplanta):
        for i in self.__listaCabañas:
            if i.getPlanta() == xplanta and i.getEstado() == 'Disponible':
                print(f"""
                       Nombre: {i.getNombre()}
                       Ubicacion: {i.getUbi()}
                       """)
                print(i)

    def buscarId(self,xid):
        i = 0
        encontrado = False
        while i < self.__listaCabañas and not encontrado:
            if i.getId() == xid:
                encontrado = True
            else:
                i += 1
        return encontrado
    
    def registrar(self,xid,xnro,xcantDias):
        i = 0
        while i < self.__listaCabañas:
            if i.buscarId(xid) and i.getNro() == xnro:
                if i.getEstado() == 'Disponible':
                    i.setEstado('Alquilada')
                    i.getCantDiasAlq(xcantDias)
            else:
                i += 1

    def mostrarIngTotal(self):
        acum = 0
        for i in self.__listaCabañas:
            if i.getEstado() == 'Disponible':
                acum += i.getCosto()
        return acum        
    
    def calcular(self,xid):
        total = 0
        for i in self.__listaCabañas:
            if i.buscarId() and i.getEstado() == 'Alquilada':
                total += i.getCosto()
        print(f"Total recaudado en el complejo {xid}: {total}")

    def ingresoTotal(self):
        print(f"Nombre: {self.__nombre}")
        acum = 0
        for cabaña in self.__listaCabañas:
            if cabaña.getEstado() == 'Disponible':
                acum += cabaña.getCosto()
        print(f"Ingreso Total: {acum}")                        