"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""
from animal_exotico import AnimalExotico
from huron import Huron
from boa_constrictor import BoaConstrictor

huron = Huron("Camilo", 100.0, 50, "colombia", 150.0)
print(f"la Informacion del huron es: {huron.__dict__}")
print(f"el sonido del huron es: {huron.hacer_sonido()}")

boa = BoaConstrictor("jose", 80.0, 100, "peru", 102.0)
boa.agregar_raton()
print(f"la Informacion de la boa es: {boa.__dict__}")
print(f"el sonido del huron es: {boa.hacer_sonido()}")
print(f"la cantidad de ratones conidos es: {boa.obtener_raton_comidos()}")
print(f"El valor de flete es: {boa.calcular_flete()}")


print("icg")