from BilleteraV import BilleteraV
from Controlador import Controlador

def test():
    unalista = Controlador()
    for i in range(3):
        print(f"\n---BILLETERA #{i+1}---")

        titular = input("Ingrese el titular de la BV: ")
        numero_celular = input("Ingrese el nro de celu: ")
        alias = input("Ingrese el alias de la BV: ")
        saldo = float(input("Ingrese saldo: "))

        unaBille = BilleteraV(titular,numero_celular,alias,saldo)
        
        print(unaBille)
        
        importe = float(input("Ingrese dinero a depositar: "))
        unaBille.IngresarDinero(importe)

        imp = float(input("Ingrese dinero a pagar por una compra: "))
        valor = unaBille.PagarCompra(imp)
        if(valor < 0):
            print("No hay saldo suficiente para pagar dicho importe")
        else:
            print(unaBille)
        unalista.agregar(unaBille)  

    #unalista.mostrar()
    unalista.recorre()
    alias = input("Ingrese alias: ")
    unalista.buscarAlias(alias)