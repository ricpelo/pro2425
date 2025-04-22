"""
El juego de la vida orientado a objetos y gráfico.
Copyright (c) 2025 Yo.
Licencia GPL-3.
"""

import random

class Celda:
    """Una celda del juego."""

    def __init__(self, viva: bool = False):
        self.__viva = viva

    def esta_viva(self) -> bool:
        """¿Está viva la celda?"""
        return self.__viva

    def revivir(self) -> None:
        """Marca la celda como viva."""
        self.__viva = True

    def matar(self) -> None:
        """Marca la celda como muerta."""
        self.__viva = False

    def __repr__(self):
        return f'Celda({self.esta_viva()!r})'


class Tablero:
    """El tablero del juego de la vida."""

    def __init__(self, ancho: int, alto: int):
        self.__ancho = ancho
        self.__alto = alto
        # self.__celdas: list[list[Celda]] = []
        # for y in range(alto):
        #     self.__celdas.append([])
        #     for _ in range(ancho):
        #         self.__celdas[y].append(Celda(random.choice([False, True])))
        self.__celdas: list[list[Celda]] = [
            [Celda(random.choice([False, True])) for _ in range(ancho)]
            for _ in range(alto)
        ]

    def ancho(self) -> int:
        """Devuelve el ancho del tablero."""
        return self.__ancho

    def alto(self) -> int:
        """Devuelve el alto del tablero."""
        return self.__alto

    def celda(self, col: int, fila: int) -> Celda:
        """Devuelve la celda situada en la posición (fila, col) del tablero."""
        return self.__celdas[fila % self.alto()][col % self.ancho()]

    def contar_vecinas_vivas(self, col: int, fila: int) -> int:
        """
        Cuenta cuántas celdas vecinas vivas tiene la celda situada en la
        posición (fila, col) del tablero.
        """
        total = 0
        total += 1 if self.celda(fila - 1, col - 1).esta_viva() else 0
        total += 1 if self.celda(fila - 1, col).esta_viva() else 0
        total += 1 if self.celda(fila - 1, col + 1).esta_viva() else 0
        total += 1 if self.celda(fila, col - 1).esta_viva() else 0
        total += 1 if self.celda(fila, col + 1).esta_viva() else 0
        total += 1 if self.celda(fila + 1, col - 1).esta_viva() else 0
        total += 1 if self.celda(fila + 1, col).esta_viva() else 0
        total += 1 if self.celda(fila + 1, col + 1).esta_viva() else 0
        return total

    def siguiente_generacion(self) -> None:
        """Pasa a la siguiente generación del tablero."""
        nuevo_tablero: list[list[Celda]] = []
        for y in range(self.alto()):
            self.__celdas.append([])
            for x in range(self.ancho()):
                esta_viva = self.celda(x, y).esta_viva()
                vecinas_vivas = self.contar_vecinas_vivas(x, y)
                if esta_viva:
                    if vecinas_vivas <= 1 or vecinas_vivas > 3:
                        self.__celdas[y][x] = Celda(False)
                    elif vecinas_vivas in [2, 3]:
                        self.__celdas[y][x] = Celda(True)
                else:
                    if vecinas_vivas == 3:
                        self.__celdas[y][x] = Celda(True)
                    else:
                        self.__celdas[y][x] = Celda(False)
        self.__celdas = nuevo_tablero



    def celdas(self):
        return self.__celdas


t = Tablero(3, 5)
print(t.celdas())
print(t.celda(2, 1))
