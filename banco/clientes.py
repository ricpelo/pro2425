"""
El módulo de los clientes del banco.
"""

from collections.abc import Iterator

class Cliente:
    """Un cliente del banco."""

    def __init__(self, dni: str, nombre: str) -> None:
        self.__set_dni(dni)
        self.set_nombre(nombre)
        self.__productos = []

    def __set_dni(self, dni: str) -> None:
        """Asigna el DNI del cliente."""
        self.__dni = dni

    def get_dni(self) -> str:
        """Devuelve el DNI del cliente."""
        return self.__dni

    def set_nombre(self, nombre: str) -> None:
        """Asigna el nombre del cliente."""
        self.__nombre = nombre

    def get_nombre(self) -> str:
        """Devuelve el nombre del cliente."""
        return self.__nombre

    def agregar_producto(self, producto) -> None:
        """Añade el producto al cliente como titular del mismo."""
        self.__productos.append(producto)

    def eliminar_producto(self, producto) -> None:
        """Elimina el producto como uno de los productos del cliente."""
        self.__productos.remove(producto)

    def get_productos(self) -> Iterator:
        """Devuelve un iterador con los productos del cliente."""
        return iter(self.__productos)
