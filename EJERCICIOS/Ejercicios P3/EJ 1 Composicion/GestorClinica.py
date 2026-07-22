from Clinica import Clinica
import csv

class GestorClinica:
    __listaC: list

    def __init__(self):
        self.__listaC = []

    def agregarClinica(self,unaClinica):
        self.__listaC.append(unaClinica)

    def cargaClinica(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/EJ 1 Composicion/clinicas.csv','r') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                unaClinica = Clinica(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                self.agregarClinica(unaClinica)        
        
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/EJ 1 Composicion/consultorios.csv','r') as archivoC:
            readerC = csv.reader(archivoC, delimiter=';')
            next(readerC)
            for fila in readerC:
                    idC = int(fila[0])
                    nroC = int(fila[1])
                    piso = int(fila[2])
                    espec = fila[3]
                    costo = float(fila[4])
                    estado = fila[5]
                    for clinica in self.__listaC:
                        if clinica.getId() == idC:
                            clinica.agregarConsultorio(idC, nroC, piso, espec, costo, estado)

    def agregarConsultorioClinica(self,idC,nroC,piso,espec,costo,estado):
        i=0
        encontrado = False
        while i < len(self.__listaC) and not encontrado:
            if self.__listaC[i].getId() == idC:
                self.__listaC[i].agregarConsultorio(idC,nroC,piso,espec,costo,estado)
                encontrado = True
                print("Consultorio agregado correctamente")
            else:
                i+=1
        if not encontrado:
            print(f"Clinica {idC} no encontrada")                                   
    
    def buscarConsultorio(self, xnro):
        i = 0
        encontrado = False
        while i < len(self.__listaC) and not encontrado:
            if self.__listaC[i].getNroC() == xnro:
                encontrado = self.__listaC[i]
            else:
                i += 1
        return encontrado
    
    def registrarOcupado(self, xnroC):
        consultorio = self.buscarConsultorio(xnroC)  
        if consultorio:
            if consultorio.registrarNroC(xnroC):
                print(f"Consultorio {xnroC} registrado correctamente.")
            else:
                print(f"No se pudo registrar el consultorio {xnroC}.")
        else:
            print("Consultorio no encontrado")                

    def registrarLibre(self, xnro):
        consultorio = self.buscarConsultorio(xnro)       
        if consultorio:
            if consultorio.liberarNroC(xnro):
                print(f"Consultorio {xnro} liberado correctamente.")
            else:
                print(f"No se pudo liberar el consultorio {xnro}.") 
        else:
            print("Consultorio no encontrado")

    """def registrarOcupado(self,xnroC):
        i=0
        registrado = False
        while i < len(self.__listaC) and not registrado:
            if self.__listaC[i].getNroC() == xnroC:
                registrado = True
                if self.__listaC[i].registrarNroC(xnroC):
                    print(f"Consultorio {xnroC} registrado correctamente.")
                else:
                    print(f"No se pudo registrar el consultorio {xnroC}.")
            else:
                i+=1
        if not registrado:
            print("Consultorio no encontrado")              

    def registrarLibre(self,xnro):
        i=0
        liberado = False
        while i < len(self.__listaC) and not liberado:
            if self.__listaC[i].getNroC() == xnro:
                liberado = True
                if self.__listaC[i].liberarNroC(xnro):
                    print(f"Consultorio {xnro} liberado correctamente.")
                else:
                    print(f"No se pudo liberar el consultorio {xnro}.") 
            else:
                i+=1
        if not liberado:
            print("Consultorio no encontrado")"""

    def mostrarMenorAMayor(self, xesp):
        i = 0
        encontrado = False
        while i < len(self.__listaC) and not encontrado:
            lista_consul = self.__listaC[i].getListaC()
            encontrado = True
            j = 0
            reencontrado = False
            while j < len(lista_consul) and not encontrado:
                if lista_consul[j].getEspecialidad() == xesp:
                    reencontrado = True
                else:
                    j += 1
            if not encontrado:
                i += 1
        if reencontrado:
            for k in range(len(self.__listaC)):
                self.__listaC[k].getListaC().sort()
                for consul in self.__listaC[k].getListaC():
                    if consul.getEspecialidad() == xesp:
                        print(f"""
                               Nro Consultorio: {consul.getNroC()}
                               Piso: {consul.getPiso()}
                               Estado: {consul.getEstado()}
                               """)
        else:
            print("Especialidad no encontrada en ninguna clínica.")

    def mostrarCantidadPorPiso(self,xnom):
        i=0
        encontrado = False
        while i < len(self.__listaC) and not encontrado:
            if self.__listaC[i].getNombre() == xnom:
                encontrado = True
            else:
                i+=1
        if encontrado:
            clinicaA = self.__listaC[i]
            for piso in range(clinicaA.getCantP()):
                contador = 0
                for consul in clinicaA.getListaC():
                    if consul.getPiso() == piso and consul.getEstado() == "Libre":
                        contador += 1
                print(f"Piso {piso} tiene {contador} consultorios libres.")  
        else:
            print(f"La clinica {xnom} no fue encontrada.")                           

    def mostrarPorEspecialidad(self):
        especialidad = ["Cardiología", "Pediatría", "Traumatología", "Clínica Médica"]
        for esp in especialidad:
            print(f"Especialidad: {esp}")
            print(f"{'Numero'}{'Piso'}{'Costo diario'}{'Estado'}")    
            for clinica in self.__listaC:
                for consul in clinica.getListaC():
                    if consul.getEspecialidad().lower() == esp.lower():
                        print(f"{consul.getNroC()}{consul.getPiso}{consul.getCosto()}{consul.getEstado()}")
