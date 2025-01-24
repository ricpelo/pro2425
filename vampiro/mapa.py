"""
Módulo de clases relacionadas con el mapa del juego.
"""

class Lugar:
    """Un lugar del juego."""
    def __init__(self, nombre: str, descripcion: str):
        self.__nombre = nombre
        self.__descripcion = descripcion

    def nombre(self):
        """El nombre del lugar."""
        return self.__nombre

    def descripcion(self):
        """La descripción del lugar."""
        return self.__descripcion
