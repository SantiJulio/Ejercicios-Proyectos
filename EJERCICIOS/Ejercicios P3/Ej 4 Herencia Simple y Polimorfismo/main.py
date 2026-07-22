from ClaseLista import ClaseLista
from ExcursionesTerrestres import ExcursionTerrestre
from ExcursionesNauticas import ExcursionNautica 

def mostrarMenu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Agregar excursión manualmente")
    print("2. Validar tipo de excursión por posición (Usa IndexError e isinstance)")
    print("3. Mostrar cantidad de excursiones de cada tipo")
    print("4. Recorrer y mostrar todas las excursiones (Nombre, Destino e Importe Final)")
    print("5. Salir")

if __name__ == '__main__':
    GE = ClaseLista()
    GE.leerExcursiones()
    opcion = 0
    while opcion != 5:
        mostrarMenu()
        entrada = input("Seleccione una opcion entre (1-5): ")
        if entrada.isnumeric():
            opcion = int(entrada)
            if opcion == 1:
                tipo = input("Ingrese el tipo de excursión (Terrestre/Nautica): ")
                nom = input("Ingrese el nombre de la excursión: ")
                des = input("Ingrese el destino de la excursión: ")
                pre = float(input("Ingrese el precio base de la excursión: "))
                if tipo == 'Terrestre':
                    km = float(input("Ingrese los km recorridos: "))
                    alm = input("¿Incluye almuerzo? (True/False): ")
                    alm = True if alm.lower() == 'true' else False
                    excursion = ExcursionTerrestre(km, alm, nom, des, pre)
                    GE.crearYAgregarExcursion(excursion)
                elif tipo == 'Nautica':
                    dur = input("Ingrese la duración en horas: ")
                    cMax = int(input("Ingrese la cantidad máxima de pasajeros: "))
                    excursion = ExcursionNautica(dur, cMax, nom, des, pre)
                    GE.crearYAgregarExcursion(excursion)
            elif opcion == 2:
                pass
            elif opcion == 3:
                GE.mostrarCantidad()   
            elif opcion == 4:
                GE.mostrarNomDesPreF()