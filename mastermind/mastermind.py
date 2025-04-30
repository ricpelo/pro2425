"""
El juego del Mastermind.

Copyright (c) 2025 1.º DAW

Licencia GNU GPL-3
"""

from abc import ABC, abstractmethod


MAX_INTENTOS = 15   # Número máximo de intentos del jugador


class Color:
    """Un color de una bola."""

    def __init__(self, nombre: str):
        self.__nombre = nombre

    def __repr__(self) -> str:
        return f'Color({self.__nombre!r})'

    def __str__(self) -> str:
        return self.__nombre


Color.BLANCO = Color('BLANCO')
Color.NEGRO = Color('NEGRO')

Color.VERDE = Color('VERDE')
Color.AZUL = Color('AZUL')
Color.AMARILLO = Color('AMARILLO')
Color.NARANJA = Color('NARANJA')


class Bola(ABC):
    """Una bola."""

    def __init__(self, color: Color):
        if color not in self.colores_permitidos():
            raise ValueError('El color no está permitido.')
        self.__color = color

    def color(self) -> Color:
        """Devuelve el color de la bola."""
        return self.__color

    @abstractmethod
    def colores_permitidos(self) -> list[Color]:
        """La lista de colores permitidos según el tipo de bola."""


class BolaPista(Bola):
    """Una bola que representa una pista al jugador."""

    def colores_permitidos(self) -> list[Color]:
        return [Color.BLANCO, Color.NEGRO]

    def es_blanca(self) -> bool:
        """Devuelve True si la bola es blanca."""
        return self.color() == Color.BLANCO

    def es_negra(self) -> bool:
        """Devuelve True si la bola es negra."""
        return self.color() == Color.NEGRO

    @staticmethod
    def crear_blanca():
        """Crea una bola blanca."""
        return BolaPista(Color.BLANCO)

    @staticmethod
    def crear_negra():
        """Crea una bola negra."""
        return BolaPista(Color.NEGRO)


class BolaJuego(Bola):
    """Una bola del juego."""

    def colores_permitidos(self) -> list[Color]:
        return [Color.AZUL, Color.VERDE, Color.AMARILLO, Color.NARANJA]
