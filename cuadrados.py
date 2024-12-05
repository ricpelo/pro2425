"""
Ejercicios de cuadrados.
"""

from itertools import count

def cuadrado(n: int) -> list[list[int]]:
    """Devuelve un cuadrado de n * n con los números del 1 al n."""
    c = count(1)
    res = []
    for _ in range(n):
        res.append([next(c) for _ in range(n)])
    return res


def imprimir_cuadrado(c: list[list[int]]) -> None:
    """Imprime el cuadrado generado por la función cuadrado()."""
    for fila in c:
        for e in fila:
            print(f"{e:3}", end=' ')
        print()


def magico(n: int) -> list[list[int]]:
    """Devuelve el cuadrado mágico de n * n (n impar)."""
    res = [[0] * n for _ in range(n)]
    c = count(1)
    fila, col = 0, n // 2
    for _ in range(n * n):
        res[fila][col] = next(c)
        # nueva_fila = n - 1 if fila == 0 else fila - 1
        # nueva_col = 0 if col == n - 1 else col + 1
        nueva_fila, nueva_col = (fila - 1) % n, (col + 1) % n
        if res[nueva_fila][nueva_col] != 0:
            nueva_fila, nueva_col = fila + 1, col
        fila, col = nueva_fila, nueva_col
    return res


def comprobar_magico(c: list[list[int]]) -> bool:
    """Comprueba si un cuadrado es mágico."""
    pass


imprimir_cuadrado(magico(5))
