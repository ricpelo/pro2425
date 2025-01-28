"""
El vocabulario del juego.
"""

class Categoria:
    """
    Las categorías de las palabras del vocabulario.
    """

class Palabra:
    """
    Las palabras que entiende el juego.
    """
    def __init__(self, lexemas: list[str], categoria: Categoria):
        self.__lexemas = lexemas
        self.__categoria = categoria

    def lexemas(self) -> list[str]:
        """Devuelve el lexema de la palabra."""
        return self.__lexemas

    def categoria(self) -> Categoria:
        """Devuelve la categoría de la palabra."""
        return self.__categoria

verbo = Categoria()
nombre = Categoria()

norte = Palabra(["norte", "n"], verbo)
sur = Palabra(["sur", "s"], verbo)
palanca = Palabra(["palanca"], nombre)
fin = Palabra(["fin", "acabar", "terminar", "finalizar"], verbo)
