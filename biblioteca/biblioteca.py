"""
La biblioteca.
"""

from datetime import datetime

class Lector:
    """
    Un lector de la biblioteca.
    """

    def __init__(self, numero: int, nombre: str, apellidos: str) -> None:
        self.__set_numero(numero)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_moroso(False)

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_numero() == otro.get_numero()

    def __hash__(self) -> int:
        return hash(self.get_numero())

    def __str__(self) -> str:
        return f'({self.get_numero()}) {self.get_nombre()} {self.get_apellidos()}'

    def __repr__(self) -> str:
        return f'Lector({self.get_numero()!r}, {self.get_nombre()!r}, {self.get_apellidos()!r})'

    def get_numero(self) -> int:
        """Devuelve el número del lector."""
        return self.__numero

    def __set_numero(self, numero: int):
        """Asigna el número del lector."""
        if numero <= 0:
            raise ValueError("El número no puede ser negativo.")
        self.__numero = numero

    def get_nombre(self) -> str:
        """Devuelve el nombre del lector."""
        return self.__nombre

    def set_nombre(self, nombre: str):
        """Asigna el nombre del lector."""
        self.__nombre = nombre

    def get_apellidos(self) -> str:
        """Devuelve los apellidos del lector."""
        return self.__apellidos

    def set_apellidos(self, apellidos: str):
        """Asigna los apellidos del lector."""
        self.__apellidos = apellidos

    def get_moroso(self) -> bool:
        """¿El lector es moroso?."""
        return self.__moroso

    def set_moroso(self, moroso: bool):
        """Asigna la morosidad del lector."""
        self.__moroso = moroso


class Libro:
    """
    Un libro de la biblioteca.
    """

    def __init__(self, codigo: str, titulo: str, autor: str, editorial: str) -> None:
        self.__set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_editorial(editorial)
        self.set_prestado(False)

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_codigo() == otro.get_codigo()

    def __hash__(self) -> int:
        return hash(self.get_codigo())

    def __set_codigo(self, codigo: str) -> None:
        """Asigna el código del libro."""
        self.__codigo = codigo

    def set_titulo(self, titulo: str) -> None:
        """Asigna el título del libro."""
        self.__titulo = titulo

    def set_autor(self, autor: str) -> None:
        """Asigna el autor del libro."""
        self.__autor = autor

    def set_editorial(self, editorial: str) -> None:
        """Asigna la editorial del libro."""
        self.__editorial = editorial

    def set_prestado(self, prestado: bool) -> None:
        """Asigna si el libro está prestado o no."""
        self.__prestado = prestado

    def get_codigo(self) -> str:
        """Devuelve el código del libro."""
        return self.__codigo

    def get_titulo(self) -> str:
        """Devuelve el título del libro."""
        return self.__titulo

    def get_autor(self) -> str:
        """Devuelve el autor del libro."""
        return self.__autor

    def get_editorial(self) -> str:
        """Devuelve la editorial del libro."""
        return self.__editorial

    def esta_prestado(self) -> bool:
        """Devuelve si el libro está prestado."""
        return self.__prestado


class Prestamo:
    """
    Un préstamo de un libro a un lector.
    """

    __lista_prestamos: list['Prestamo'] = []

    @staticmethod
    def buscar_prestamo_vigente(libro: Libro) -> 'Prestamo | None':
        """
        Busca un préstamo de un determinado libro que esté aún pendiente
        de devolver.
        """
        for prestamo in Prestamo.__lista_prestamos:
            if prestamo.get_libro() == libro and prestamo.esta_vigente():
                return prestamo
        return None

    def __init__(
        self,
        libro: Libro,
        lector: Lector,
        fecha_prestamo: datetime = datetime.now()
    ) -> None:
        if libro.esta_prestado():
            raise ValueError("El libro ya está prestado.")
        self.__set_libro(libro)
        self.__set_lector(lector)
        self.__set_fecha_prestamo(fecha_prestamo)
        self.__set_fecha_devolucion(None)
        Prestamo.__lista_prestamos.append(self)

    def get_libro(self) -> Libro:
        """Devuelve el libro del préstamo."""
        return self.__libro

    def get_lector(self) -> Lector:
        """Devuelve el lector del préstamo."""
        return self.__lector

    def get_fecha_prestamo(self) -> datetime:
        """Devuelve la fecha del préstamo."""
        return self.__fecha_prestamo

    def get_fecha_devolucion(self) -> datetime | None:
        """Devuelve la fecha de devolución del préstamo."""
        return self.__fecha_devolucion

    def __set_libro(self, libro: Libro):
        """Asigna el libro del préstamo."""
        self.__libro = libro

    def __set_lector(self, lector: Lector):
        """Asigna el lector del préstamo."""
        self.__lector = lector

    def __set_fecha_prestamo(self, fecha_prestamo: datetime):
        """Asigna la fecha del préstamo."""
        if fecha_prestamo < datetime.now():
            raise ValueError("No se puede prestar en el pasado.")
        self.__fecha_prestamo = fecha_prestamo

    def __set_fecha_devolucion(self, fecha_devolucion: datetime | None):
        """Asigna la fecha de devolución del préstamo."""
        if fecha_devolucion is not None and fecha_devolucion < self.get_fecha_prestamo():
            raise ValueError("No se puede devolver antes de prestarlo.")
        self.__fecha_devolucion = fecha_devolucion

    def esta_vigente(self):
        """Indica si el préstamo está vigente."""
        return self.get_fecha_devolucion() is None

    def devolver(self) -> None:
        """Devuelve el préstamo."""
        assert self.get_libro().esta_prestado()
        self.__set_fecha_devolucion(datetime.now())
        self.get_libro().set_prestado(False)
        diferencia = datetime.now() - self.get_fecha_prestamo()
        if diferencia.days > 15:
            self.get_lector().set_moroso(True)
