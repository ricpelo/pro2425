"""
El módulo de los clientes del banco.
"""

from collections.abc import Iterator

class Cliente:
    """Un cliente del banco."""

    __clientes: dict[str,'Cliente'] = {}

    @staticmethod
    def buscar_por_dni(dni: str) -> 'Cliente | None':
        """
        Busca un cliente por su DNI. Devuelve None si no lo encuentra.
        """
        return Cliente.__clientes.get(dni)

    @staticmethod
    def clientes() -> Iterator['Cliente']:
        """Recorre todos los clientes."""
        return Cliente.__clientes.values()

    def __init__(self, dni: str, nombre: str) -> None:
        self.__set_dni(dni)
        self.set_nombre(nombre)
        self.__productos = []
        Cliente.__clientes[dni] = self

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_dni() == otro.get_dni()

    def __hash__(self) -> int:
        return hash(self.get_dni())

    def __str__(self) -> str:
        return f'{self.get_dni()} {self.get_nombre()}'

    def __repr__(self) -> str:
        return f'Cliente({self.get_dni()!r}, {self.get_nombre()!r})'

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
