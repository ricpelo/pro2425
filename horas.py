"""
Ejercicio 3 de Relaciones entre clases
"""

class Hora:
    """Instantes de tiempo con horas y minutos."""

    def __init__(self, hora, minutos):
        self.set_hora(hora)
        self.set_minutos(minutos)

    def get_hora(self) -> int:
        """Devuelve la hora."""
        return self.__hora

    def set_hora(self, hora) -> bool:
        """Asigna la hora."""
        if hora in range(0, 24):
            self.__hora = hora
            return True
        return False

    def get_minutos(self) -> int:
        """Devuelve los minutos."""
        return self.__minutos

    def set_minutos(self, minutos) -> bool:
        """Asigna los minutos."""
        if minutos in range(0, 60):
            self.__minutos = minutos
            return True
        return False

    def inc(self) -> None:
        """Incrementa en un minuto."""
        if self.get_minutos() < 59:
            self.set_minutos(self.get_minutos() + 1)
        else:
            self.set_minutos(0)
            if self.get_hora() < 23:
                self.set_hora(self.get_hora() + 1)
            else:
                self.set_hora(0)

    def __str__(self) -> str:
        return f'{self.get_hora():02}:{self.get_minutos():02}'

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_hora() == otro.get_hora() and \
                self.get_minutos() == otro.get_minutos()

    def __hash__(self) -> int:
        return hash((self.get_hora(), self.get_minutos()))


class HoraExacta(Hora):
    """Una hora que contiene también los segundos."""

    def __init__(self, hora, minutos, segundos):
        super().__init__(hora, minutos)
        self.set_segundos(segundos)

    def get_segundos(self) -> int:
        """Devuelve los segundos."""
        return self.__segundos

    def set_segundos(self, segundos) -> bool:
        """Asigna los segundos."""
        if segundos not in range(0, 60):
            return False
        self.__segundos = segundos
        return True

    def inc(self) -> None:
        """Incrementa un segundo."""
        if self.get_segundos() < 59:
            self.set_segundos(self.get_segundos() + 1)
        else:
            self.set_segundos(0)
            super().inc()

    def __str__(self) -> str:
        return super().__str__() + f':{self.get_segundos():02}'

    def __eq__(self, otro) -> bool:
        if not hasattr(otro, 'get_segundos') and self.get_segundos() != 0:
            return False
        if not isinstance(otro, type(self)):
            return NotImplemented
        return super().__eq__(otro) and self.get_segundos() == otro.get_segundos()

    def __hash__(self) -> int:
        return super().__hash__()


def incrementar(h: Hora) -> None:
    """Incrementa."""
    h.inc()


h1 = Hora(23, 4)
h2 = HoraExacta(23, 4, 0)
h3 = HoraExacta(23, 4, 1)
print(h1 == h2)
s = set({h1, h2})
print(hash(h1))
print(hash(h2))
print(h2 == h3)
print(hash(h2))
print(hash(h3))
