"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 3: Pruebas y Errores
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""
import unittest

from huron import Huron

class TestHuron(unittest.TestCase):
    
    def setUp(self):
        # Crea una instancia de Huron antes de cada prueba
        self.huron = Huron(nombre="Furioso", peso=1.2, edad=3, pais_origen="España", impuestos=0.1)
    
    def test_atributos_huron(self):
        # Prueba para verificar los atributos del objeto huron
        print(self.huron.__dict__)  # Correcto: imprime todos los atributos del objeto huron
        self.assertEqual(self.huron.nombre, "Furioso")
        self.assertEqual(self.huron.peso, 1.2)
        self.assertEqual(self.huron.edad, 3)
        self.assertEqual(self.huron.pais_origen, "España")
        self.assertEqual(self.huron.impuestos, 0.1)
    
    def test_hacer_sonido(self):
        # Prueba de método hacer_sonido
        sonido = self.huron.hacer_sonido()
        self.assertEqual(sonido, "¡Eek Eek!")


if __name__ == "__main__":
    unittest.main()
