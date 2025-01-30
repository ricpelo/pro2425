"""
El vocabulario del juego.
"""

class Categoria:
    """
    Las categorías de las palabras del vocabulario.
    """


class Vocabulario:
    """El vocabulario de la aventura."""
    def __init__(self):
        self.__palabras: dict[str, Palabra] = {}

    def insertar(self, palabra: 'Palabra') -> 'Vocabulario':
        """Insertar una palabra en el vocabulario."""
        for lexema in palabra.lexemas():
            self.__palabras[lexema] = palabra
        return self

    def insertar_varias(self, palabras: list['Palabra']):
        """Inserta varias palabras en el vocabularios."""
        for palabra in palabras:
            self.insertar(palabra)

    def buscar(self, lexema: str) -> 'Palabra|None':
        """
        Devuelve la palabra que tenga un cierto lexema, o None si no existe.
        """
        return self.__palabras.get(lexema)


class Palabra:
    """
    Las palabras que entiende el juego.
    """

    vocabulario = Vocabulario()

    def __init__(self, lexemas: list[str], categoria: Categoria):
        self.__lexemas = lexemas
        self.__categoria = categoria
        Palabra.vocabulario.insertar(self)

    def lexemas(self) -> list[str]:
        """Devuelve el lexema de la palabra."""
        return self.__lexemas

    def categoria(self) -> Categoria:
        """Devuelve la categoría de la palabra."""
        return self.__categoria


cat_verbo = Categoria()
cat_nombre = Categoria()

norte = Palabra(["norte", "n"], cat_verbo)
sur = Palabra(["sur", "s"], cat_verbo)
este = Palabra(["este", "e"], cat_verbo)
oeste = Palabra(["oeste", "o"], cat_verbo)
palanca = Palabra(["palanca"], cat_nombre)
fin = Palabra(["fin", "acabar", "terminar", "finalizar"], cat_verbo)

# vocabulario = Vocabulario()
# # vocabulario.insertar(norte).insertar(sur).insertar(palanca).insertar(fin)
# vocabulario.insertar_varias([norte, sur, este, oeste, palanca, fin])
