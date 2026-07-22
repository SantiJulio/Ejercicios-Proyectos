from GestorProducto import GestorProducto
from ProductoFisica import ProductoFisica
from ProductoLinea import ProductoLinea

def mostrarMenu():
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

if __name__ == '__main__':
    GP = GestorProducto()
    GP.cargaProducto()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione un numero entre (1-4)")
        opcion = int(entrada)
        if opcion == 1:
            tipo = input("Ingrese el tipo de producto: ")
            cod = input("Ingrese el codigo del mismo: ")
            nom = input("Ingrese el nombre: ")
            pre = float(input("Ingrese precio: "))
            desc = input("Ingrese descripcion: ")
            stock = int(input("Ingrese stock: "))
            if tipo == 'Online':
                url = input("Ingrese url: ")
                porc = int(input("Ingrese porcentaje: "))
                envio = input("Es gratis el envio?")
                envio = True if envio.lower() == 'true' else False
                costo = int(input("Ingrese costo de envio: "))
                producto = ProductoLinea(url,porc,envio,costo,cod,nom,pre,desc,stock) 
                GP.crearYagregarPro(producto)
            elif tipo == 'Fisica':
                dir = input("Ingrese direccion: ")
                tasa = int(input("Ingrese tasa de impuesto: "))
                producto = ProductoFisica(dir,tasa,cod,nom,pre,desc,stock)  
                GP.crearYagregarPro(producto)   
        if opcion == 2:
            xcod = input("Ingrese un producto a vender: ")
            GP.ventaUnProducto(xcod) 
        elif opcion == 3:
            GP.mostrarNombre()     
        elif opcion == 4:
            GP.mostrarTodo()