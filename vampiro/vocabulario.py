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

    @staticmethod
    def decodificar_entrada(entrada: str) -> 'tuple[Palabra|None, Palabra|None]':
        """Decodifica la entrada del jugador."""
        palabras = entrada.split()
        verbo, nombre = None, None
        if len(palabras) == 0:
            return (None, None)
        if len(palabras) > 2:
            print("No entiendo lo que dices.")
            return (None, None)
        verbo = Palabra.vocabulario.buscar(palabras[0])
        if verbo is None or verbo.categoria() != cat_verbo:
            print("No entiendo lo que dices.")
            return (None, None)
        if len(palabras) == 2:
            nombre = Palabra.vocabulario.buscar(palabras[1])
            if nombre is not None and nombre.categoria() != cat_nombre:
                print("No entiendo lo que dices.")
                return (None, None)
        return (verbo, nombre)


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
