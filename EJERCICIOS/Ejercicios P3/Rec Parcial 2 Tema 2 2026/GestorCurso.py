from ClaseLista import Lista
from Curso import Curso
from Estudiante import Estudiante
import csv

class Gestor:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregar(self,unCurso): #para reutilizar codigo se manda a la clase Lista
        self.__lista.agregarCurso(unCurso)
    
    def cargaCurso(self):
        archivo = open('cursos.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            unCurso = Curso(int(fila[0]),fila[1],fila[2],int(fila[3]),float(fila[4]),int(fila[5]),fila[6])
            self.cargaEstudiante(unCurso)
            self.agregar(unCurso)
        archivo.close()

    def cargaEstudiante(self,curso):
        archivo = open('estudiantes.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            if curso.getId() == fila[0]:
                unEstudiante = Estudiante(fila[1],fila[2],int(fila[3]),fila[4],fila[5])
                curso.agregarEstudiantes(unEstudiante)
        archivo.close()

    def instanciarEstudiante(self,id,nom,ape,dni,correo,ciudad):
        unEstudiante = Estudiante(nom,ape,dni,correo,ciudad)
        try:
            self.__lista.buscarCurso(id,unEstudiante)
        except ValueError:
            print("Cupo insuficiente.")        

    def buscarEst(self,xdni):
        self.__lista.buscarEstudiante(xdni)

    def buscarCat(self,xcat):
        self.__lista.buscarCategoria(xcat)

    def buscar(self,xdni):
        self.__lista.calcular(xdni)

    def validarPos(self,pos):
        self.__lista.mostrarPorPos(pos)                        