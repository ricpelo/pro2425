"""
Módulo de clases relacionadas con el mapa del juego.
"""

import vocabulario as v

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

    def describir(self):
        """Describe el lugar."""
        print(self.nombre())
        print(self.descripcion())

class Mapa:
    """
    El mapa del juego.
    """
    def __init__(self):
        self.__mapeado = {}

    def insertar(self, lugar: Lugar, conexiones: dict):
        """Mete en el mapa un lugar con sus conexiones."""
        self.__mapeado[lugar] = conexiones

    def conexiones(self, lugar: Lugar) -> dict:
        """Devuelve las conexiones de un lugar."""
        return self.__mapeado[lugar]

    def salida_hacia(self, lugar: Lugar, direccion: v.Palabra) -> Lugar|None:
        """
        Qué salida hay desde un lugar hacia una dirección.
        Devuelve None si no hay salida hacia esa dirección.
        """
        return self.__mapeado[lugar].get(direccion)


vestibulo = Lugar("VESTÍBULO", "Estás en el vestíbulo del castillo. Bla bla bla...")
pasillo = Lugar("PASILLO", "Te encuentras en medio del pasillo principal de este piso.")
mapa = Mapa()
mapa.insertar(vestibulo, {v.norte: pasillo})
mapa.insertar(pasillo, {v.sur: vestibulo})
