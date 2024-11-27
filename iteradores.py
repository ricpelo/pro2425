from itertools import cycle, repeat

def emparejar(lista: list) -> list:
    return [(i, e) for i, e in zip(repeat(0), lista)]


print(emparejar(['a', 'b', 'c', 'd']) == [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')])
print(emparejar(['a', 'b', 'c', 'd']))


def parejas(filas, columnas):
#    return [(x, y) for x in range(filas) for y in range(columnas)]
    res = []
    for fila in range(filas):
        for columna in range(columnas):
            res.append((fila, columna))
    return res


print(parejas(4, 3))
