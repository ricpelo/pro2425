"""
Ejercicio del hotel.
"""

from abc import ABC, abstractmethod
import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree # type: ignore
from persistent import Persistent


class Habitacion(Persistent, ABC):
    """Una habitación del hotel."""

    def __init__(self, numero: int):
        self.__numero = numero

    def numero(self) -> int:
        """Devuelve el número de la habitación."""
        return self.__numero

    @abstractmethod
    def precio_por_noche(self) -> float:
        """Devuelve el precio por noche de la habitación."""


class Simple(Habitacion, Persistent):
    """Una habitación simple."""

    def precio_por_noche(self) -> float:
        return 20.0


class Doble(Habitacion, Persistent):
    """Una habitación doble."""

    def precio_por_noche(self) -> float:
        return 40.0


class Suite(Habitacion, Persistent):
    """Una suite."""

    def precio_por_noche(self) -> float:
        return 80.0


class Reserva(Persistent):
    """Una reserva."""

    def __init__(self, dni: str, habitacion: Habitacion, noches: int):
        self.__dni = dni
        self.__habitacion = habitacion
        self.__noches = noches

    def dni(self) -> str:
        """Devuelve el DNI del cliente de la reserva."""
        return self.__dni

    def habitacion(self) -> Habitacion:
        """Devuelve la habitación reservada."""
        return self.__habitacion

    def noches(self) -> int:
        """Devuelve el número de noches que se ha reservado."""
        return self.__noches

    def coste_total(self) -> float:
        """Coste total de la reserva."""
        return self.habitacion().precio_por_noche() * self.noches()


class Hotel(Persistent):
    """Un hotel."""

    def __init__(self):
        self.__habitaciones = BTree()
        self.__reservas = BTree()

    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al hotel."""
        if habitacion.numero() not in self.__habitaciones:
            self.__habitaciones[habitacion.numero()] = habitacion

    def reservar(self, dni: str, numero_habitacion: int, noches: int) -> Reserva:
        """Reserva una habitación a un cliente para un número de noches."""

        habitacion = self.__habitaciones[numero_habitacion]
        if habitacion.numero() in self.__reservas:
            raise ValueError("Habitación ya reservada.")
        res = Reserva(dni, habitacion, noches)
        self.__reservas[habitacion.numero()] = res
        return res


hotel = Hotel()
hotel.agregar_habitacion(Simple(100))
hotel.agregar_habitacion(Suite(200))
r1 = hotel.reservar('11111111A', 100, 3)
r2 = hotel.reservar('22222222B', 200, 5)
print(r1.coste_total())
print(r2.coste_total())

almacen = ZODB.FileStorage.FileStorage("hotel.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

raiz['hotel'] = hotel
transaction.commit()
conexion.close()
bd.close()
