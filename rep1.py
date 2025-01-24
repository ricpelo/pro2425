"""
Escribir en Python una función llamada
cifrar_mensaje(texto) que implemente un cifrado de tipo «César», de forma que
cada letra es sustituida por la siguiente en el alfabeto (se entiende que la
siguiente de la «z» es la «a»). Los caracteres no alfabéticos no se deben
sustituir, y hay que mantener las mayúsculas y minúsculas.
Indicación: usar las funciones ord() y chr().
Ejemplos:
cifrar_mensaje(’¡Hola, Mundo!’) => ’¡Ipmb, Nvoep!’
"""

def cifrar_mensaje(texto: str) -> str:
    """Cifra mensaje."""
    res = []
    for c in texto:
        if c.isalpha():
            if c == 'Z':
                r = 'A'
            else:
                r = chr(ord(c) + 1)
        else:
            r = c
        res.append(r)
    return "".join(res)

print(cifrar_mensaje('¡Hola, Mundo!') == '¡Ipmb, Nvoep!')


def traspuesta(matriz: list[list]) -> list[list]:
    """Calcula la traspuesta de la matriz."""
    num_filas = len(matriz)
    if num_filas == 0:
        return [[]]
    num_columnas = len(matriz[0])
    return [[matriz[i][j] for i in range(num_filas)] for j in range(num_columnas)]

print(traspuesta([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(traspuesta([[8, 7, 4], [2, 9, 5]]))


def es_anagrama(c1: str, c2: str) -> bool:
    """Determina si son anagramas uno del otro."""
    return sorted(c1.lower()) == sorted(c2.lower())


def suma_digitos(numero: int) -> bool:
    """¿Es divisible por la suma de sus dígitos?"""
    return numero % sum(int(x) for x in str(numero)) == 0
