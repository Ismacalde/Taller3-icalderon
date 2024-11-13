"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 3: Pruebas y Errores
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""

import unittest
from boa_constrictor import BoaConstrictor


class TestBoaConstrictor(unittest.TestCase):
    
    def setUp(self):
         # Crea una instancia de Huron antes de cada prueba
        self.boa = BoaConstrictor(nombre="Serpentina",  peso=3.0, edad=5, pais_origen="Brasil", impuestos=0.2)  

    def test_atributos_BoaConstrictor(self):
        # Prueba para verificar los atributos del objeto Boa
        print(self.boa.__dict__)  # Correcto: imprime todos los atributos del objeto Boa
        self.assertEqual(self.boa.nombre, "Serpentina")
        self.assertEqual(self.boa.peso, 3.0)
        self.assertEqual(self.boa.edad, 5)
        self.assertEqual(self.boa.pais_origen, "Brasil")
        self.assertEqual(self.boa.impuestos, 0.2)

    def test_hacer_sonido(self):
        sonido = self.boa.hacer_sonido()
        self.assertEqual(sonido, "¡Tsss!")  

    def test_calcular_flete(self):
        flete = self.boa.calcular_flete()
        self.assertEqual(flete, 0.6)
   

    def test_alimentar(self):
    # Verificar que el contador de ratones aumenta y lanza un error al llegar a 10
        for _ in range(20):
           self.boa.agregar_raton()
        with self.assertRaises(ValueError) as context:
            self.boa.agregar_raton()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")


if __name__ == "__main__":
    unittest.main()