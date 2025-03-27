"""
El ejercicio de las lámparas y las bombillas.
"""

class Bombilla:
    """Una bombilla."""

    def __init__(self, potencia: float, tamanyo: str):
        if potencia < 0:
            raise ValueError("No puede haber bombillas con potencia negativa.")
        if tamanyo not in ('P', 'M'):
            raise ValueError("La bombilla tiene que ser pequeña o mediana.")
        self.__potencia = potencia
        self.__tamanyo = tamanyo

    def potencia(self) -> float:
        """La potencia en vatios de la bombilla."""
        return self.__potencia

    def tamanyo(self) -> str:
        """El tamaño de la bombilla."""
        return self.__tamanyo


class Lampara:
    """Una lámpara."""

    def __init__(self, num_pequenyos: int, num_medianos: int, potencia_maxima: float):
        if num_pequenyos < 0 or num_medianos < 0 or potencia_maxima < 0:
            raise ValueError("No se puede.")
        self.__num_casquillos: dict[str, int] = { 'P': num_pequenyos, 'M': num_medianos }
        self.__potencia_maxima = potencia_maxima
        self.__bombillas: dict[str, list[Bombilla]] = { 'P': [], 'M': [] }

    def poner(self, bombilla: Bombilla) -> 'Lampara':
        """Pone una bombilla en la lámpara."""
        tamanyo = bombilla.tamanyo()
        if len(self.__bombillas[tamanyo]) >= self.__num_casquillos[tamanyo]:
            return self
        if self.potencia_total() + bombilla.potencia() > self.__potencia_maxima:
            return self
        self.__bombillas[tamanyo].append(bombilla)
        return self

    def quitar(self, tamanyo: str) -> Bombilla | None:
        """Quita una bombilla de la lámpara."""
        if len(self.__bombillas[tamanyo]) == 0:
            return None
        return self.__bombillas[tamanyo].pop()

    def potencia_total(self) -> float:
        """Devuelve la potencia total consumida por la lámpara."""
        suma = 0
        for lista_bombillas in self.__bombillas.values():
            for bombilla in lista_bombillas:
                suma += bombilla.potencia()
        return suma


print(Lampara(3, 0, 20).poner(Bombilla(10, 'P')).potencia_total())
print(Lampara(3, 0, 20).poner(Bombilla(10, 'M')).potencia_total())
print(Lampara(3, 2, 20).poner(Bombilla(10, 'P')).poner(Bombilla(10, 'M')).quitar('M').tamanyo())
