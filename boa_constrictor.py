"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""

from animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        """ Inicializa una nueva Boa Constrictor. """
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0  # Inicializa la cuenta de ratones comidos

    def hacer_sonido(self) -> str:
        """ Retorna el sonido característico de la boa constrictor. """
        return "¡Tsss!"

    def agregar_raton(self) -> None:
        """ Incrementa la cuenta de ratones comidos por la boa constrictor. """
        if self._ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += 1

    def obtener_raton_comidos(self) -> int:
        """ Devuelve la cantidad de ratones comidos. """
        return self._ratones_comidos

    def calcular_flete(self) -> float:
        """ Calcula el costo de importar a la boa constrictor basado en impuestos y peso. """
        return round(self.impuestos * self.peso, 2)

    def obtener_informacion(self) -> str:
        return f"Sonido: {self.hacer_sonido()} - Ratones comidos: {self.obtener_raton_comidos()}"
