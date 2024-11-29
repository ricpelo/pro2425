"""
Histograma de una cadena.
"""


def distribucion(s: str) -> dict[str, int]:
    """Devuelve la distribución de repeticiones de los caracteres de una cadena."""
    res = {}
    for c in s:
#        res[c] = 1 if c not in res else res[c] + 1
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def histograma(s: str) -> None:
    """Dibuja el histograma de una cadena."""
    for c, n in distribucion(s).items():
        print(c, '=' * n, n)


cadena = "Esto es una prueba de cadena de ejemplo"
print(distribucion(cadena))
histograma(cadena)
