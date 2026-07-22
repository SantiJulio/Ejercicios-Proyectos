from Consultorio import Consultorio

class Clinica:
    __id: int
    __nom: str
    __direccion: str
    __director: str
    __cantP: int
    __listaCons: list

    def __init__(self,id,nom,direccion,director,cantP):
        self.__id = id
        self.__nom = nom
        self.__direccion = direccion
        self.__director = director
        self.__cantP = cantP
        self.__listaCons = []

    def agregarConsultorio(self,idC,nroC,piso,esp,costo,estado):
        unConsultorio = Consultorio(idC,nroC,piso,esp,costo,estado)
        self.__listaCons.append(unConsultorio)

    def getId(self):
        return self.__id

    def getNom(self):
        return self.__nom

    def getCantP(self):
        return self.__cantP

    def getListaCons(self):
        return self.__listaCons

    def __str__(self):
        return (f"""
                ID: {self.__id}
                Nombre: {self.__nom}
                Cant Pisos: {self.__cantP}
                 """)  

    def buscarConsul(self,xnum):
        i = 0
        encontrado = None
        while i < self.__listaCons and not encontrado: 
            if i.getNroC() == xnum:
                encontrado = self.__listaCons[i]      
            else:
                i += 1
        return encontrado              

    def Ocupado(self,xnum):
        consul = self.buscarConsul(xnum) 
        if consul is not None and consul.getEstado() == "Libre":
            consul.setEstado("Ocupado")  
            return True
        return False

    def Liberar(self,xnum):
        consul = self.buscarConsul(xnum)
        if consul is not None and consul.getEstado() == "Ocupado":
            consul.setEstado("Libre") 
            return True
        return False                         

    def mostrarEspec(self,xe):
        self.__listaCons.sort()
        for i in range(len(self.__listaCons)):
            if self.__listaCons[i].getEsp() == xe:
                print(f"""
                       Numero: {self.__listaCons[i].getNroC()}
                       Piso: {self.__listaCons[i].getPiso()}
                       Estado: {self.__listaCons[i].getEstado()}
                       """) 

    def libresPorPiso(self,xid):
        for i in range(self.__cantP):
            cant = 0
            for j in range(len(self.__listaCons)):
                if self.__listaCons[i].getId() == xid and self.__listaCons[i].getEstado() == 'Libre':
                    cant += 1
            if cant > 0:
                print(f"En el piso {i} tiene {cant} libres")        
            else:
                print(f"El piso {i} no tiene consultorios libres")                         

    def mostrarTodo(self):
        especialidad = ["Cardiología", "Pediatría", "Traumatología", "Clínica Médica"]
        for esp in especialidad:
            print(f"Especialidad: {esp}")
            print(f"{'Numero'}{'Piso'}{'Costo diario'}{'Estado'}")
            for i in len(self.__listaCons):
                if self.__listaCons[i].getEsp() == esp:
                    print(f"""
                           Numero: {self.__listaCons[i].getNroC()}
                           Piso: {self.__listaCons[i].getPiso}
                           Costo Diario: {self.__listaCons[i].getCosto()}
                           Estado: {self.__listaCons[i].getEstado()}
                           """)                    