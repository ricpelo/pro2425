"""
Módulo que implementa el jugador de la aventura.
"""

from mapa import Lugar, mapa
import vocabulario as v

class Jugador:
    """El jugador."""
    def __init__(self, inicial: Lugar):
        self.__lugar = inicial

    def lugar(self) -> Lugar:
        """El lugar actual del jugador."""
        return self.__lugar

    def mover(self, nuevo: Lugar) -> None:
        """Mueve al jugador al nuevo lugar."""
        self.__lugar = nuevo

    def intentar_mover(self, direccion: v.Palabra) -> None:
        """Intenta mover al jugador hacia la dirección indicada."""
        salida = mapa.salida_hacia(self.lugar(), direccion)
        if salida is None:
            print("No hay salida en esa dirección.")
        else:
            self.mover(salida)
            salida.describir()
