from Producto import Producto
from ProductoFisica import ProductoFisica
from ProductoLinea import ProductoLinea
import csv

class GestorProducto:
    __listaP: list

    def __init__(self):
        self.__listaP = []

    def agregarProducto(self,producto):
        self.__listaP.append(producto)

    def cargaProducto(self):
        with open('D:/Documents/SANTI/PROGRAMACION WEB/POO 2026/EJERCICIOS/Ejercicios P3/Extra Parcial 2 2025/productos.csv', 'r') as archivo:
            reader = csv.reader(archivo,delimiter=',')    
            next(reader)
            for fila in reader:
                tipo = fila[0]
                cod = fila[1]
                nom = fila[2]
                precio = float(fila[3])
                desc = fila[4]
                stock = int(fila[5])
                if tipo == 'Online':
                    url = fila[6]
                    porc = int(fila[7])
                    envio = fila[8].strip().lower() == 'true'
                    costo = int(fila[9])
                    producto = ProductoLinea(url,porc,envio,costo,cod,nom,precio,desc,stock) 
                elif tipo == 'Fisica':
                    dir = fila[10]
                    tasa = int(fila[11])
                    producto = ProductoFisica(dir,tasa,cod,nom,precio,desc,stock)  
                self.agregarProducto(producto)   

    """def crearYagregarPro(self,producto):
        i = 0
        encontrado = False
        if isinstance(producto, Producto):
            while i < len(self.__listaP) and not encontrado:
                if producto.getCodigo() == self.__listaP[i].getCodigo():
                    encontrado = True
                else:
                    i+=1 
            if encontrado:
                raise ValueError 
            else:
                self.agregarProducto(producto)
                print("Se agrego el producto correctamente.")""" 

    def crearYagregarPro(self,producto):
        i = 0
        encontrado = False
        if isinstance(producto, Producto):
            while i < len(self.__listaP) and not encontrado:
                if producto.getCodigo() == self.__listaP[i].getCodigo():
                    encontrado = True
                else:
                    i+=1 
            if not encontrado:
                self.agregarProducto(producto)
                print("Se agrego el producto correctamente.") 
        else:
            raise ValueError 

    def ventaUnProducto(self,xcod):
        i = 0
        encontrado = False
        while i < len(self.__listaP) and not encontrado:
            if self.__listaP[i].getCodigo() == xcod:
                encontrado = True
                if self.__listaP[i].getStock():
                    self.__listaP[i].actualizarStock()
                    print("Se actualizo el stock.")
                else:
                    print("No tiene stock.")
            else:
                i+=1 

    def mostrarNombre(self):
        for i in range(len(self.__listaP)):
            if type(self.__listaP[i]) == ProductoLinea:
                if self.__listaP[i].getPorcD() > 10 and self.__listaP[i].getEnvio():
                    print(f"Nombre: {self.__listaP[i].getNombre}")

    def mostrarTodo(self):
        for i in range(len(self.__listaP)):
            self.__lista[i].mostrar()                       