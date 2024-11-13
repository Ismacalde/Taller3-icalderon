"""
curso: COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - EDCO_202420_CUR-0043962_GRU_02
Taller 4: Herencia (POO)”
Autor: Ismael Calderon
correo: icalderon@cesconsultoria.com
"""
# animal.py
from abc import ABC, abstractmethod
from ianimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre:str, peso:float, edad:int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self.kilos_comidos=0

    def comer(self, kilos: int) -> None:
        self.kilos_comidos+=kilos

    def obtener_kilos_comidos(self):
        return self.kilos_comidos

    @abstractmethod
    def hacer_sonido(self) :   
        pass
    
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self._nombre

    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
    
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo privado 'peso' """
        return self._peso

    @peso.setter
    def peso(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')

    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self._edad

    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'edad'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')
        
        


