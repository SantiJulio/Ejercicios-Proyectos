from Estudiante import Estudiante

class Curso:
    __id: int
    __nombre: str
    __docente: str
    __duracion: int
    __importeMensual: float
    __cupo: int
    __categoria: str
    __listaEstudiantes: list

    def __init__(self,id,nom,doc,dur,imp,cupo,cat):
        self.__id = id
        self.__nombre = nom
        self.__docente = doc
        self.__duracion = dur
        self.__importeMensual = imp
        self.__cupo = cupo
        self.__categoria = cat

    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDuracion(self):
        return self.__duracion
    
    def getImporteMensual(self):
        return self.__importeMensual

    def getCupo(self):
        return self.__cupo
    
    def getCategoria(self):
        return self.__categoria
    
    def agregarEstudiante(self,unEstudiante):
        self.__listaEstudiantes.append(unEstudiante)

    def asignarAlumno(self,objeto):
        if len(self.__listaEstudiantes) < self.__cupo:
            self.cargaEstudiantes(objeto)

    def buscarDNI(self,xdni):
        i = 0
        encontrado = False
        while i < len(self.__listaEstudiantes) and not encontrado:
            if self.__listaEstudiantes[i].getDni() == xdni:
                encontrado = True
            else:
                i += 1 
        if encontrado:
            print(f"""
                   Nombre: {self.__listaEstudiantes[i].getNombre()}
                   Apellido: {self.__listaEstudiantes[i].getApellido()}
                   Inscripto en el curso: {self.__nombre}
                   Duracion: {self.__duracion}
                   """)  
        else:
            print(f"No se encuentra inscripto en: {self.__nombre}")

    def verificarCuPo(self):
        if len(self.__listaEstudiantes) == self.__cupo:
            print(f"Curso {self.__nombre} posee cupo acabado.")            

    def verificarDnI(self,xdni):
        i = 0
        encontrado = False
        while i < len(self.__listaEstudiantes) and not encontrado:
            if self.__listaEstudiantes[i].getDni() == xdni:
                encontrado = True
            else:
                i += 1
        if encontrado:
            importe = self.__importeMensual
            return importe 

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Duracion: {self.__duracion}")
        for estudiante in self.__listaEstudiantes:
            print(estudiante)                       