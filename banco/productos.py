"""
Módulo de gestión de los productos del banco.
"""

from abc import ABC, abstractmethod

class Operacion:
    """Una operación realizada sobre un producto."""

    def __init__(self, fecha_hora: str, concepto: str, importe: float) -> None:
        self.__set_fecha_hora(fecha_hora)
        self.__set_concepto(concepto)
        self.__set_importe(importe)

    def get_fecha_hora(self):
        """Devuelve la fecha y hora de la operación."""
        return self.__fecha_hora

    def get_concepto(self):
        """Devuelve el concepto de la operación."""
        return self.__concepto

    def get_importe(self):
        """Devuelve el importe de la operación."""
        return self.__importe

    def __set_fecha_hora(self, fecha_hora):
        """Asigna la fecha y hora de la operación."""
        self.__fecha_hora = fecha_hora

    def __set_concepto(self, concepto):
        """Asigna el concepto de la operación."""
        self.__concepto = concepto

    def __set_importe(self, importe):
        """Asigna el importe de la operación."""
        self.__importe = importe


class Producto(ABC):
    """Un producto del banco."""

    def __init__(self, numero: int) -> None:
        self.__set_numero(numero)

    def __set_numero(self, numero: int) -> None:
        """Asigna el número del producto."""
        self.__numero = numero

    def get_numero(self):
        """Devuelve el número del producto."""
        return self.__numero

    @abstractmethod
    def total(self) -> float:
        """Devuelve el total del producto."""
        ...
