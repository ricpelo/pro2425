"""
El juego de la vida orientado a objetos y gráfico.
Copyright (c) 2025 Yo.
Licencia GPL-3.
"""

import tkinter as tk
import random


ANCHO_TABLERO = 60    # Número de celdas horizontales
ALTO_TABLERO = 60     # Número de celdas verticales
TAMANYO_CELDA = 10    # Tamaño de cada celda en píxeles horiz. y vert.
RETARDO = 50          # Retardo en milisegundos entre generaciones


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

    def __init__(self, ancho: int, alto: int, tamanyo_celda: int, ventana: tk.Tk):
        self.__ancho = ancho
        self.__alto = alto
        self.__tamanyo_celda = tamanyo_celda
        # self.__celdas: list[list[Celda]] = []
        # for y in range(alto):
        #     self.__celdas.append([])
        #     for _ in range(ancho):
        #         self.__celdas[y].append(Celda(random.choice([False, True])))
        self.__celdas: list[list[Celda]] = [
            [Celda(random.choice([False, True])) for _ in range(ancho)]
            for _ in range(alto)
        ]
        self.__canvas = tk.Canvas(
            ventana,
            width = ancho * tamanyo_celda,
            height = alto * tamanyo_celda,
            bg="black"
        )
        self.__canvas.pack()
        self.dibujar()

    def ancho(self) -> int:
        """Devuelve el ancho del tablero."""
        return self.__ancho

    def alto(self) -> int:
        """Devuelve el alto del tablero."""
        return self.__alto

    def tamanyo_celda(self) -> int:
        """Devuelve el tamaño de la celda en píxeles."""
        return self.__tamanyo_celda

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
        nuevo_tablero: list[list[Celda]] = [
            [Celda(False) for _ in range(self.ancho())]
            for _ in range(self.alto())
        ]
        for y in range(self.alto()):
            for x in range(self.ancho()):
                esta_viva = self.celda(x, y).esta_viva()
                vecinas_vivas = self.contar_vecinas_vivas(x, y)
                if (esta_viva and vecinas_vivas in [2, 3]) or \
                   (not esta_viva and vecinas_vivas == 3):
                    nuevo_tablero[y][x].revivir()
        self.__celdas = nuevo_tablero

    def dibujar(self) -> None:
        """Dibuja el tablero en el canvas."""
        self.__canvas.delete('all')
        for y in range(self.alto()):
            for x in range(self.ancho()):
                if self.celda(x, y).esta_viva():
                    x1 = x * self.tamanyo_celda()
                    y1 = y * self.tamanyo_celda()
                    x2 = x1 + self.tamanyo_celda()
                    y2 = y1 + self.tamanyo_celda()
                    self.__canvas.create_rectangle(x1, y1, x2, y2, fill="white")


class JuegoDeLaVida(tk.Tk):
    """La clase principal."""

    def __init__(self, ancho: int, alto: int, tamanyo_celda: int, retardo: int):
        super().__init__()
        self.title('Juego de la vida')
        self.__tablero = Tablero(ancho, alto, tamanyo_celda, self)
        self.__retardo = retardo
        self.after(retardo, self.actualizar)

    def actualizar(self):
        """Calcula la siguiente generación y la visualiza."""
        self.__tablero.siguiente_generacion()
        self.__tablero.dibujar()
        self.after(self.__retardo, self.actualizar)


app = JuegoDeLaVida(ANCHO_TABLERO, ALTO_TABLERO, TAMANYO_CELDA, RETARDO)
app.mainloop()
