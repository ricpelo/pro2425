"""
Ejercicio 3 de Relaciones entre clases
"""

class Hora:
    """Instantes de tiempo con horas y minutos."""
    def __init__(self, hora, minutos):
        self.set_hora(hora)
        self.set_minutos(minutos)

    def set_hora(self, hora) -> bool:
        """Asigna la hora."""
        if hora in range(0, 24):
            self.__hora = hora
            return True
        return False

    def set_minutos(self, minutos) -> bool:
        """Asigna los minutos."""
        if minutos in range(0, 60):
            self.__minutos = minutos
            return True
        return False

    def inc(self) -> None:
        """Incrementa en un minuto."""
        if self.__minutos < 59:
            self.__minutos += 1
        else:
            self.__minutos = 0
            if self.__hora < 23:
                self.__hora += 1
            else:
                self.__hora = 0

    def __str__(self) -> str:
        return f'{self.__hora:02}:{self.__minutos:02}'

    """
    Implementar método __eq__
    """

h1 = Hora(23, 4)
h2 = Hora(23, 4)
print(h1 == h2)
