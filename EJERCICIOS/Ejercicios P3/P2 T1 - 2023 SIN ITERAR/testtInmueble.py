import unittest
from Casa import Casa
from Departamento import Departamento

class TestImporteInmueble(unittest.TestCase):

    def testImporteVentaCasa(self):
        localidad = "Rivadavia"
        direccion = "CPN Dr. Jose Olmos 333"
        supCub = 500
        metros = 200
        pruebaCasa = Casa(localidad,direccion,supCub,metros)

        valorEstimado = 45000000

        self.assertAlmostEqual(pruebaCasa.importeVenta(),valorEstimado)

    def testImporteVentaDpto(self):
        localidad = "Chimbas"
        direccion = "Reconquista 2556"
        supCub = 300
        cantidadDormitorios = 3
        nroMono = 26 
        nroDpto = 7
        piso = 3
        pruebaDpto = Departamento(localidad,direccion,supCub,cantidadDormitorios,nroMono,nroDpto,piso)

        valorEstimado = 10000000

        self.assertAlmostEqual(pruebaDpto.importeVenta(),valorEstimado)     