"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)”
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""
# animal_exotico.py
from animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        # Inicializa la clase padre
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen  # Nuevo atributo: país de origen
        self.impuestos = impuestos        # Nuevo atributo: impuestos

    def calcular_flete(self) -> float:
        """
        Calcula el costo de importar el animal multiplicando los impuestos por el peso del animal.
        """
        return round(self.impuestos * self.peso, 2)

    @property
    def pais_origen(self) -> str:
        """ Devuelve el país de origen del animal exótico. """
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value: str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'origen'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise ValueError('Expected str for pais_origen')

    @property
    def impuestos(self) -> float:
        """ Devuelve el valor de los impuestos del animal exótico. """
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value: float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'impuestos'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float for impuestos')
