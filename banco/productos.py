"""
Módulo de gestión de los productos del banco.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator
from datetime import datetime
from clientes import Cliente

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

    def __str__(self) -> str:
        return f'{self.get_fecha_hora()} | {self.get_concepto()} {self.get_importe()}'


class Producto(ABC):
    """Un producto del banco."""

    def __init__(self, numero: int, titular: Cliente) -> None:
        self.__set_numero(numero)
        self.__set_titular(titular)
        titular.agregar_producto(self)
        self.__operaciones: list[Operacion] = []

    def __set_titular(self, titular: Cliente) -> None:
        """Asigna el titular del producto."""
        self.__titular = titular

    def __set_numero(self, numero: int) -> None:
        """Asigna el número del producto."""
        self.__numero = numero

    def get_numero(self) -> int:
        """Devuelve el número del producto."""
        return self.__numero

    def get_titular(self) -> Cliente:
        """Devuelve el titular del producto."""
        return self.__titular

    def agregar_operacion(self, op: Operacion) -> None:
        """Añade una operación al producto."""
        self.__operaciones.append(op)

    def mostrar_operaciones(self):
        """Muestra las operaciones relizadas sobre el producto."""
        for op in self:
            print(op)

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Producto):
            return NotImplemented
        return self.get_numero() == otro.get_numero()

    def __hash__(self) -> int:
        return hash(self.get_numero())

    def __iter__(self) -> Iterator[Operacion]:
        """Devuelve un iterador que recorre las operaciones del producto."""
        return iter(self.__operaciones)

    @abstractmethod
    def total(self) -> float:
        """Devuelve el total del producto."""
        ...


class CuentaCorriente(Producto):
    """Una cuenta corriente del banco."""

    def __init__(self, numero: int, titular: Cliente) -> None:
        super().__init__(numero, titular)
        self.__saldo = 0.0

    def total(self) -> float:
        return self.__saldo

    def agregar_movimiento(self, concepto: str, importe: float):
        """Agrega un movimiento a la cuenta."""
        fecha_hora = datetime.now().isoformat(' ')[:19]
        self.agregar_operacion(Operacion(fecha_hora, concepto, importe))
        self.__saldo += importe
