"""
El ejercicio de las lámparas y las bombillas.
"""

class Tamanyo:
    """El tamaño de un casquillo o una bombilla."""
    def __init__(self, tamanyo: str):
        self.__tamanyo = tamanyo

    def __repr__(self):
        return f'Tamanyo({self.__tamanyo!r})'


PEQUENYO = Tamanyo('P')
MEDIANO = Tamanyo('M')


class Bombilla:
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


class Casquillo:
    """Un casquillo de la lámpara."""

    def __init__(self, tamanyo: Tamanyo):
        self.__tamanyo = tamanyo
        self.__bombilla: Bombilla | None = None

    def tamanyo(self) -> Tamanyo:
        """Devuelve el tamaño del casquillo."""
        return self.__tamanyo

    def bombilla(self) -> Bombilla | None:
        """Devuelve la bombilla que está en el casquillo, o None si no hay."""
        return self.__bombilla

    def poner(self, bombilla: Bombilla):
        """Pone una bombilla en el casquillo."""
        if self.tamanyo() != bombilla.tamanyo():
            raise ValueError("Los tamaños no coinciden.")
        self.__bombilla = bombilla

    def quitar(self) -> Bombilla | None:
        """Quita la bombilla que hay en el casquillo, si hay alguna."""
        bombilla = self.__bombilla
        self.__bombilla = None
        return bombilla

    def esta_vacio(self) -> bool:
        """Devuelve True si el casquillo está vacío."""
        return self.__bombilla is None


class Lampara:
    """Una lámpara."""

    def __init__(self, num_pequenyos: int, num_medianos: int, potencia_maxima: float):
        if num_pequenyos < 0 or num_medianos < 0 or potencia_maxima < 0:
            raise ValueError("No se puede.")
        self.__potencia_maxima = potencia_maxima

        # Crea los casquillos dentro de la lámpara:
        self.__casquillos: set[Casquillo] = set()
        for _ in range(num_pequenyos):
            self.__casquillos.add(Casquillo(PEQUENYO))
        for _ in range(num_medianos):
            self.__casquillos.add(Casquillo(MEDIANO))

    def poner(self, bombilla: Bombilla) -> 'Lampara':
        """Pone una bombilla en la lámpara."""
        if self.potencia_total() + bombilla.potencia() > self.__potencia_maxima:
            return self

        for casquillo in self.__casquillos:
            if casquillo.tamanyo() == bombilla.tamanyo() and casquillo.esta_vacio():
                casquillo.poner(bombilla)
                break
        return self

    def quitar(self, tamanyo: Tamanyo) -> Bombilla | None:
        """Quita una bombilla de la lámpara."""
        for casquillo in self.__casquillos:
            if casquillo.tamanyo() == tamanyo and not casquillo.esta_vacio():
                return casquillo.quitar()
        return None

    def potencia_total(self) -> float:
        """Devuelve la potencia total consumida por la lámpara."""
        suma = 0
        for casquillo in self.__casquillos:
            if not casquillo.esta_vacio():
                suma += casquillo.bombilla().potencia()
        return suma


print(Lampara(3, 0, 20).poner(Bombilla(10, PEQUENYO)).potencia_total())
print(Lampara(3, 0, 20).poner(Bombilla(10, MEDIANO)).potencia_total())
print(Lampara(3, 2, 20).poner(Bombilla(10, PEQUENYO)).poner(Bombilla(10, MEDIANO)).quitar(MEDIANO).tamanyo())
