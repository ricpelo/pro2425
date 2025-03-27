"""
Ejercicio de puertas y llaves.
"""

class Llave:
    """Una llave."""

    def __init__(self, color: str):
        self.__color = color

    def color(self) -> str:
        """El color de la llave."""
        return self.__color


class Puerta:
    """Una puerta."""

    def __init__(self, color: str):
        self.__color = color
        self.__llave: Llave | None = None
        self.__abierta = False

    def poner(self, llave: Llave) -> 'Puerta':
        """Pone una llave en la cerradura de la puerta."""
        self.__llave = llave
        return self

    def quitar(self) -> Llave | None:
        """Quita la llave de la puerta, si la hay."""
        llave = self.__llave
        self.__llave = None
        return llave

    def abrir(self) -> bool:
        """Abre la puerta."""
        if self.__abierta:
            return True
        if self.__llave is not None and self.__llave.color() == self.__color:
            self.__abierta = True
            return True
        return False

    def cerrar(self) -> None:
        """Cierra la puerta."""
        self.__abierta = False


assert Puerta('rojo').poner(Llave('rojo')).abrir()
assert not Puerta('rojo').poner(Llave('verde')).abrir()
assert not Puerta('rojo').abrir()
