from BilleteraV import BilleteraV

class Controlador:
    __arreBille = list
    def __init__(self):
        self.__arreBille = []

    def agregar(self, unaBille):
        if isinstance(unaBille,BilleteraV):
            self.__arreBille.append(unaBille)

    def mostrar(self):
        for BilleteraV in self.__arreBille:
            print(BilleteraV)

    def recorre(self):
        for BilleteraV in self.__arreBille:
            if BilleteraV.get_Saldo() < 0:
                print(BilleteraV.get_Alias())

    def buscarAlias(self, alias):
        i = 0
        while i < len(self.__arreBille) and self.__arreBille[i].get_Alias() != alias:
            i+=1
        if(i < len(self.__arreBille)):
            importe = float(input("Ingrese dinero a tranferir"))    
            self.__arreBille[i].IngresarDinero(importe)
            print("Tranferencia exitosa")
        else:
            print("El alias ingresado no existe")    