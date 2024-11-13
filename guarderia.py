# En guarderia.py

from boa_constrictor import BoaConstrictor
from huron import Huron

class Guarderia ():

    def __init__(self):
        self.boas = [BoaConstrictor("Brasil", 15.0, 20), BoaConstrictor("Colombia", 12.0, 18)]
        self.hurones = [Huron("USA", 5.0, 1.5), Huron("Canadá", 6.0, 2)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.agregar_raton()
            return "Éxito"
        except ValueError:
            return "La boa está llena"
