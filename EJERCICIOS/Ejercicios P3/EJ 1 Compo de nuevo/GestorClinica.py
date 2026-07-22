from Clinica import Clinica
import csv

class GestorClinica:
    __listaCli: list

    def __init__(self):
        self.__listaCli = []

    def agregarCinica(self,clinica):
        if not isinstance(clinica,Clinica):
            raise TypeError
        else:
            self.__listaCli.append(clinica)

    def cargaCliYCons(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/EJ 1 Compo de nuevo/clinicas.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                unaClinica = Clinica(int(fila[0]), fila[1]. fila[2], fila[3], int(fila[4]))
                self.agregarCinica(unaClinica)

        with open('D:\Documents\SANTI\PROGRAMACION WEB\POO 2026\EJERCICIOS\Ejercicios P3\EJ 1 Compo de nuevo\consultorios.csv', 'r') as archivoC:
            readerC = csv.reader(archivoC,delimiter=';')
            next(readerC)
            for fila in readerC:
                idC = int(fila[0])
                nroC = int(fila[1])
                piso = int(fila[2])
                esp = fila[3]
                costo = float(fila[4])
                estado = fila[5]
                for i in len(self.__listaCli):
                    if self.__listaCli[i].getId() == idC:
                        self.__listaCli[i].agregarConsultorio(idC,nroC,piso,esp,costo,estado)

    def agregarConsulCli(self,idC,nroC,piso,esp,costo,estado):
        i = 0
        encontrado = False
        while i < len(self.__listaCli) and not encontrado:
            if isinstance(self.__listaCli[i],Clinica):
                if self.__listaCli[i].getId() == idC:
                    self.__listaCli[i].agregarConsultorio(idC,nroC,piso,esp,costo,estado)
                    encontrado = True
                else: 
                    i += 1    
            else:
                raise IndexError

    def registrarOcupado(self,xnum):
        i = 0
        encontrado = True
        while i < len(self.__listaCli) and not encontrado:
            if self.__listaCli[i].Ocupado(xnum):
                encontrado = True
            else: 
                i += 1

    def registrarLibre(self,xnum):
        i = 0
        encontrado = False
        while i < len(self.__listaCli) and not encontrado:
            if self.__listaCli[i].Liberar(xnum):
                encontrado = True
            else:
                i += 1    

    def mostrarMenorMayor(self,xe):
        for i in range(len(self.__listaCli)):
            self.__listaCli[i].mostrarEspec(xe)                       

    def cantidadLibre(self,xnom):
        i = 0
        encontrado = False
        while i < len(self.__listaCli) and not encontrado:
            if self.__listaCli[i].getNom() == xnom:
                encontrado = True
            else:
                i += 1
        if encontrado:
            self.__listaCli[i].libresPorPiso(self.__listaCli[i].getId())         

    def mostrarPorEsp(self):
        for i in range(len(self.__listaCli)):
            self.__listaCli[i].mostrarTodo()                                           