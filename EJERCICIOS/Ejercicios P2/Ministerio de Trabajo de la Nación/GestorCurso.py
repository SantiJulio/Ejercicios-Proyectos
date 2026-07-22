from Curso import Curso
import csv

class GestorCurso:
    __lista: list

    def __init__(self):
        self.__lista = []

    def cargarCurso(self,curso):
        self.__lista.append(curso)

    def leerCurso(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Ministerio de Trabajo de la Nación/cursos.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unCurso = Curso(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]))
                self.cargarCurso(unCurso)

    def buscarCursoPorId(self,xid):
        encontrado = None
        i = 0
        while i < len(self.__lista) and encontrado is None:
            if str(self.__lista[i].getIdC()) == str(xid):
                encontrado = self.__lista[i]
            i+=1
        return encontrado

    def generarReporteRechazados(self,XGI):
        for Curso in self.__lista: #Recorremos la lista de todos los cursos cargados
            idC = Curso.getIdC()
            rechazados = XGI.obtenerRechazadas(idC)
            print(f"\nCurso: {Curso.getDenominacion():<40} Cantidad de horas: {Curso.getCantH()}")
            print("Inscripciones rechazadas")
            print(f"{'DNI':<15} {'Apellido':<20} {'Nombre':<20} {'Provincia':<20}")
            print("-" * 75)
            if len(rechazados) > 0: #Si hay rechazados, los listamos. Si no, mostramos un aviso
                for ins in rechazados:
                    print(f"{ins.getDni():<15} {ins.getApellido():<20} {ins.getNombre():<20} {ins.getProvinciaP():<20}")
            else:
                print("No se registraron inscripciones rechazadas para este curso.")        