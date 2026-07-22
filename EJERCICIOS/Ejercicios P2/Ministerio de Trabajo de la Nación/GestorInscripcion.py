from Inscripcion import Inscripcion
import csv
import numpy as np

class GestorInscripcion:
    __ndarray: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int

    def __init__(self,dimension=5,incremento=5):
        self.__ndarray = np.empty(dimension, dtype = Inscripcion)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = incremento

    def cargarInscripcion(self,inscripcion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__ndarray = np.resize(self.__ndarray, self.__dimension)
        self.__ndarray[self.__cantidad] = inscripcion
        self.__cantidad += 1 

    def leerInscripcion(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P2/Ministerio de Trabajo de la Nación/Inscripciones.csv', 'r') as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                unaInscripcion = Inscripcion(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], fila[5])
                self.cargarInscripcion(unaInscripcion)

    def procesarInscripcionesRepetidas(self,xdni):
        i = 0 #Buscar la primera inscripción que coincida con ese DNI
        encontrado = False
        primera = None
        while i < self.__cantidad and not encontrado:
            if self.__ndarray[i].getDni() == xdni:
                primera = self.__ndarray[i]
                encontrado = True
            else:
                i += 1
        # 2. Si la encontramos, buscamos a la misma persona en el resto del arreglo
        if encontrado:
            print(f"Buscando duplicados para: {primera.getApellido()}, {primera.getNombre()}, {primera.getDni()}, {primera.getProvinciaP()}")
            for j in range(self.__cantidad):
                # Usamos == para que se ejecute el _eq_ de la clase Inscripcion
                # Y chequeamos 'is not' para no rechazar a la 'primera' que encontramos
                if self.__ndarray[j] == primera and self.__ndarray[j] is not primera:
                    self.__ndarray[j].setEstado('R')
                    print(f"Inscripción duplicada rechazada en el curso ID: {self.__ndarray[j].getIdCurso()}")   
        else:
            print("No se encontro ninguna inscripcion con ese DNI.")

    def procesarCupos(self,xid,xcurso):
        if xcurso is None:
            print("El curso no existe.")
            return
        cupoMax = int(xcurso.getCupoI())
        for i in range(self.__cantidad): #Recorremos el arreglo de inscripciones buscando las de este curso
            inscripcion = self.__ndarray[i]
            if str(inscripcion.getIdCurso()) == str(xid): #Verificamos si la inscripción pertenece al curso consultado
                # Si ya está 'R' (Rechazada por el punto a), se deja como está.
                if inscripcion.getEstado() == 'P':
                    if xcurso.getCupoA() < cupoMax:
                        # Si todavía hay lugar en el curso
                        inscripcion.setEstado('A')
                        xcurso.actualizarCupoA()
                    else:
                        inscripcion.setEstado('R') #Si el cupo se llenó, las siguientes pendientes se rechazan
        print(f"Inscripciones procesadas. Cupos aceptados finales: {xcurso.getCupoA()} de {cupoMax}")

    def obtenerRechazadas(self,idCurso):
        listaR = []
        for i in range(self.__cantidad):
            inscripcion = self.__ndarray[i]
            if str(inscripcion.getIdCurso()) == str(idCurso) and inscripcion.getEstado() == 'R':
                listaR.append(inscripcion)
        listaR.sort() #Llamar al método __lt__
        return listaR 

    def generarReporteAceptados(self,xidCurso):
        print(f"\nInscriptos ACEPTADOS para el curso ID: {xidCurso}")
        print(f"{'DNI':<15} {'Apellido':<20} {'Nombre':<20} {'Provincia':<20}")
        print("-" * 75)
        contadorA = 0
        for i in range(self.__cantidad):
            inscripcion = self.__ndarray[i]
            if str(inscripcion.getIdCurso()) == str(xidCurso) and inscripcion.getEstado() == 'A':
                print(f"{inscripcion.getDni():<15} {inscripcion.getApellido():<20} {inscripcion.getNombre():<20} {inscripcion.getProvinciaP():<20}")
                contadorA += 1
        if contadorA == 0:
            print("No se encontraron alumnos aceptados en este curso.")        