from abc import ABC, abstractmethod

class Figura(ABC):
    """Una figura."""

    def __init__(self, ancho: float, alto: float):
        self.set_ancho(ancho)
        self.set_alto(alto)

    def ancho(self):
        """Devuelve el ancho."""
        return self.__ancho

    def alto(self):
        """Devuelve el alto."""
        return self.__alto

    def set_ancho(self, ancho: float):
        """Asigna el ancho."""
        Figura.__comprobar_positivo(ancho)
        self.__ancho = ancho

    def set_alto(self, alto: float):
        """Asigna el alto."""
        Figura.__comprobar_positivo(alto)
        self.__alto = alto

    @staticmethod
    def __comprobar_positivo(valor):
        """Comprueba si el valor es mayor que cero."""
        if valor <= 0:
            raise ValueError("No admite valores negativos.")

    @abstractmethod
    def dibujar(self) -> None:
        """Dibuja la figura."""
        ...

    @abstractmethod
    def area(self) -> float:
        """Calcula el área de la figura."""
        ...


class Triangulo(Figura):
    """Un triángulo."""

    def dibujar(self) -> None:
        print("   *   ")
        print("  ***  ")
        print(" ***** ")
        print("*******")

    def area(self) -> float:
        return self.ancho() * self.alto() / 2.0


class Rectangulo(Figura):
    """Un rectángulo."""

    def dibujar(self) -> None:
        print("*********")
        print("*********")
        print("*********")
        print("*********")

    def area(self) -> float:
        return self.ancho() * self.alto()


def mostrar(f: Figura) -> None:
    f.dibujar()


t = Triangulo(4, 3)
t.dibujar()

r = Rectangulo(8, 5)
r.dibujar()

mostrar(t)
mostrar(r)

print(t.area())
print(r.area())

def duplicar_area_figura(f: Figura) -> float:
    return f.area() * 2.0

print(duplicar_area_figura(r))
