from Curso import Curso

class Nodo:
    __curso: Curso
    __siguiente: object

    def __init__(self,objeto):
        self.__curso = objeto
        self.__siguiente = None

    def getCurso(self):
        return self.__curso

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getId(self):
        return self.__curso.getId()

    def asignarAlumno(self,objeto):
        self.__curso.asignarAlumno(objeto)

    def buscarDni(self,xdni):
        self.__curso.buscarDNI(xdni)

    def obtenerCategoria(self):
        return self.__curso.getCategoria()     

    def verificarCupo(self):
        self.__curso.verificarCuPo()       

    def verificarDni(self,xdni):
        acum = 0
        self.__curso.verificarDnI(xdni)
        return acum  

    def mostrarDatos(self):
        self.__curso.mostrar()  