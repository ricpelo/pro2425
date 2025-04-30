"""
El juego del Mastermind.

Copyright (c) 2025 1.º DAW

Licencia GNU GPL-3
"""

MAX_INTENTOS = 15   # Número máximo de intentos del jugador

class Color:
    pass

BLANCA = Color()
NEGRA = Color()

class BolaPista:
    """Una bola que representa una pista al jugador."""

    def __init__(self, color: Color):
        self.__color = color


azul = BolaPista('verde')
