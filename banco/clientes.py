"""
El módulo de los clientes del banco.
"""

class Cliente:
    """Un cliente del banco."""

    def __init__(self, dni: str, nombre: str) -> None:
        self.__set_dni(dni)
        self.set_nombre(nombre)

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


pepe = Cliente('123123123', 'Pepe Pérez')
