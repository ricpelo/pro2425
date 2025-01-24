"""
Módulo que implementa el jugador de la aventura.
"""

from mapa import Lugar

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
