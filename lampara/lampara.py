"""
El ejercicio de las lámparas y las bombillas.
"""

import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent
from BTrees.OOBTree import BTree


class Tamanyo(Persistent):
    """El tamaño de un casquillo o una bombilla."""
    def __init__(self, tamanyo: str):
        self.__tamanyo = tamanyo

    def __repr__(self):
        return f'Tamanyo({self.__tamanyo!r})'


PEQUENYO = Tamanyo('P')
MEDIANO = Tamanyo('M')


class Bombilla(Persistent):
    """Una bombilla."""

    def __init__(self, potencia: float, tamanyo: Tamanyo):
        if potencia < 0:
            raise ValueError("No puede haber bombillas con potencia negativa.")
        self.__potencia = potencia
        self.__tamanyo = tamanyo

    def potencia(self) -> float:
        """La potencia en vatios de la bombilla."""
        return self.__potencia

    def tamanyo(self) -> Tamanyo:
        """El tamaño de la bombilla."""
        return self.__tamanyo


class Casquillo(Persistent):
    """Un casquillo de la lámpara."""

    __ultimo = 0

    def __init__(self, tamanyo: Tamanyo):
        self.__tamanyo = tamanyo
        self.__bombilla: Bombilla | None = None
        Casquillo.__ultimo += 1
        self.__numero = Casquillo.__ultimo

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.numero() == otro.numero()

    def __hash__(self):
        return hash(self.numero())

    def numero(self) -> int:
        """Devuelve el número del casquillo."""
        return self.__numero

    def tamanyo(self) -> Tamanyo:
        """Devuelve el tamaño del casquillo."""
        return self.__tamanyo

    def bombilla(self) -> Bombilla | None:
        """Devuelve la bombilla que está en el casquillo, o None si no hay."""
        return self.__bombilla

    def poner(self, bomb: Bombilla):
        """Pone una bombilla en el casquillo."""
        if self.tamanyo() != bomb.tamanyo():
            raise ValueError("Los tamaños no coinciden.")
        self.__bombilla = bomb

    def quitar(self) -> Bombilla | None:
        """Quita la bombilla que hay en el casquillo, si hay alguna."""
        bomb = self.__bombilla
        self.__bombilla = None
        return bomb

    def esta_vacio(self) -> bool:
        """Devuelve True si el casquillo está vacío."""
        return self.__bombilla is None


class Lampara(Persistent):
    """Una lámpara."""

    __ultimo = 0

    def __init__(self, num_pequenyos: int, num_medianos: int, potencia_maxima: float):
        if num_pequenyos < 0 or num_medianos < 0 or potencia_maxima < 0:
            raise ValueError("No se puede.")
        self.__potencia_maxima = potencia_maxima
        Lampara.__ultimo += 1
        self.__numero = Lampara.__ultimo

        # Crea los casquillos dentro de la lámpara:
        self.__casquillos = BTree()
        for _ in range(num_pequenyos):
            casquillo = Casquillo(PEQUENYO)
            self.__casquillos[casquillo.numero()] = casquillo
        for _ in range(num_medianos):
            casquillo = Casquillo(MEDIANO)
            self.__casquillos[casquillo.numero()] = casquillo

    def numero(self) -> int:
        """Devuelve el número de la lámpara."""
        return self.__numero

    def poner(self, bombilla: Bombilla) -> 'Lampara':
        """Pone una bombilla en la lámpara."""
        if self.potencia_total() + bombilla.potencia() > self.__potencia_maxima:
            return self

        for casquillo in self.__casquillos.values():
            if casquillo.tamanyo() == bombilla.tamanyo() and casquillo.esta_vacio():
                casquillo.poner(bombilla)
                break
        return self

    def quitar(self, tamanyo: Tamanyo) -> Bombilla | None:
        """Quita una bombilla de la lámpara."""
        for casquillo in self.__casquillos.values():
            if casquillo.tamanyo() == tamanyo and not casquillo.esta_vacio():
                return casquillo.quitar()
        return None

    def potencia_total(self) -> float:
        """Devuelve la potencia total consumida por la lámpara."""
        suma = 0
        for casquillo in self.__casquillos.values():
            if not casquillo.esta_vacio():
                suma += casquillo.bombilla().potencia()
        return suma

    def casquillos(self) -> Casquillo:
        """Devuelve los casquillos de la lámpara."""
        return self.__casquillos.values()


# print(Lampara(3, 0, 20.0).poner(Bombilla(10, PEQUENYO)).potencia_total())
# print(Lampara(3, 0, 20.0).poner(Bombilla(10, MEDIANO)).potencia_total())
# print(Lampara(3, 2, 20.0).poner(Bombilla(10, PEQUENYO)).poner(Bombilla(10, MEDIANO)).quitar(MEDIANO).tamanyo())

lamp = Lampara(3, 2, 20.0).poner(Bombilla(10, PEQUENYO)).poner(Bombilla(10, MEDIANO))

almacen = ZODB.FileStorage.FileStorage("lampara.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

raiz['lamparas'] = BTree()
raiz['lamparas'][lamp.numero()] = lamp
transaction.commit()

conexion.close()
bd.close()

del lamp
del raiz

# Volver a abrir la base de datos para recuperar la información:

almacen = ZODB.FileStorage.FileStorage("lampara.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

for lamp in raiz['lamparas'].values():
    print(lamp.potencia_total())
    for casquillo in lamp.casquillos():
        bombilla = casquillo.bombilla()
        if bombilla is not None:
            print(bombilla.tamanyo())
