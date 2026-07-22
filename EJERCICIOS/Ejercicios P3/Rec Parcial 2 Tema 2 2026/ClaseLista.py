from ClaseNodo import Nodo

class Lista:
    __cabeza: Nodo
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__tope = 0

    def getCabeza(self):
        return self.__cabeza

    def getTope(self):
        return self.__tope

    def agregarCurso(self,objeto):
        nodo = Nodo(objeto)
        nodo.setSiguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__tope += 1 

    def buscarCurso(self,cod,objeto):
        aux = self.__cabeza
        while aux is not None:
            if aux.getId() == cod:
                try:
                    aux.asignarAlumno(objeto)
                except:
                    aux = aux.getSiguiente()
            else:
                i += 1

    def buscarEstudiante(self,xdni):
        aux = self.__cabeza
        while aux is not None:
            aux = self.buscarDni(xdni)
            aux = aux.getSiguiente()

    def buscarCategoria(self,xcat):
        aux = self.__cabeza
        for aux in self.__cabeza:
            if aux.obtenerCategoria() == xcat:
                aux.verificarCupo()
            aux = aux.getSiguiente()    

    def calcular(self,xdni):
        aux = self.__cabeza
        acum = 0
        for aux in self.__cabeza:
            acum += aux.verificarDni(xdni)
            aux = aux.getSiguiente()
        print(f"Debe pagar en total {acum}") 

    def mostrarPorPos(self,pos):
        if pos < 0 or pos >= self.__tope:
            raise IndexError
        aux = self.__comienzo
        while aux is not None:
            aux = self.mostrarDatos()
            aux = aux.getSiguiente()           