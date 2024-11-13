"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""

from animal_exotico import AnimalExotico

class Huron(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        """ Inicializa un nuevo Hurón. """
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    def hacer_sonido(self) -> str:
        """ Retorna el sonido característico del hurón. """
        return "¡Eek Eek!"

    def obtener_informacion(self) -> str:
        return f" Sonido: {self.hacer_sonido()}"
