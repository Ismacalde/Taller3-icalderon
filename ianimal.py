"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)”
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""
# ianimal.py
from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def comer(self, kilos:int) -> None :   
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):    
        pass

