import unittest
from claseCasas import Casa
from claseDepartamentos import Departamento


class TestImporteDeInmuebles(unittest.TestCase):

    def testImporteDeVentaCasa(self):
        localidad = "Rivadavia"
        direccion = "Av. Ignacio de la Roza 580(e)"
        superficie = 200.0
        mts = 300.0

        prueba = Casa(localidad, direccion, superficie, mts)

        valorEstimado = 32400000000.0

        self.assertAlmostEqual(prueba.importeDeVenta(), valorEstimado)

    def testImporteDeVentaDpto(self):
        dptoPrueba = Departamento(
            localidad="Capital",
            direccion="Santa Fe 4590",
            superficie=70.0,
            cantDormitorios=2,
            numMonoblock=1,
            numDpto=4,
            piso=1,
        )

        valorEstimado = 35700000.0

        self.assertAlmostEqual(dptoPrueba.importeDeVenta(), valorEstimado)


if __name__ == "__main__":
    unittest.main()
