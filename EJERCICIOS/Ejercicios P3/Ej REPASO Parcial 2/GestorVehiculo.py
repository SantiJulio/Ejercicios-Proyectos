from Vehiculo import Vehiculo
from VehiculoAplicacion import VehiculoAplicacion
from VehiculoSucursal import VehiculoSucursal

class GestorVehiculo:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarVehiculo(self,vehiculo):
        i = 0
        encontrado = False
        if isinstance(vehiculo,Vehiculo):
            while i < len(self.__lista) and not encontrado:
                if vehiculo.getCod() == self.__lista[i].getCod():
                    encontrado = True
                else:
                    i+=1
            if encontrado:
                raise TypeError
            else:
                self.__lista.append(vehiculo)

    def buscarCod(self,xcod):
        i = 0
        encontrado = False
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getCod() == xcod:
                encontrado = True   
            else:
                i+=1   
        if encontrado:
            return encontrado 
        else: 
            return i             

    def alquilar(self,xcod):
        encontrado = self.buscarCod(xcod)
        if encontrado: 
            if self.getCantD():
                self.alquilerV()
                print("Se alquilo el vehiculo.")
            else:
                raise ValueError

    def mostrarTodo(self):
        for i in range(len(self.__lista)):
            if type(self.__lista[i]) == VehiculoAplicacion:
                if self.__lista[i].getPorcD() >= 15 and not self.__lista[i].getSeguro():
                    print(f"""
                           Marca: {self.__lista[i].getMarca()}
                           Modelo: {self.__lista[i].getModelo()}
                           """)                           

    def mostrarTodoDosPuntoCero(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrar()                            

    def calcularEinformar(self):
        cantT = 0
        cantVA = 0
        cantVS = 0
        for i in range(len(self.__lista)):
            if isinstance(self.__lista[i], Vehiculo):
                cantT += 1
                if type(self.__lista[i]) == VehiculoAplicacion:
                    cantVA += 1
                elif type(self.__lista[i]) == VehiculoSucursal:
                    cantVS += 1
            else:
                raise ValueError
            print("Esto no es un vehiculo.")            

    def buscarPorCod(self,xcod):
        encontrado = self.buscarCod(xcod)
        if encontrado:
            print()
        else:
            print("No existe")    