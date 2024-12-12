def suma2(iterable, total: int) -> list[int]:
    """
    suma2([1, 2, 3], 5) => [2, 3]
    suma2([4, 10, 8], 12) => [4, 8]
    suma2([4, 10, 8], 24) => []
    """
    for i, e1 in enumerate(iterable):
        for e2 in iterable[i + 1:]:
            if e1 + e2 == total:
                return [e1, e2]
    return []


assert suma2([1, 2, 3], 5) == [2, 3]
assert suma2([4, 10, 8], 12) == [4, 8]
assert suma2([4, 10, 8], 24) == []


def clasificar(estudiantes: dict[str, float]) -> dict[str, list[str]]:
    """
    clasificar({"Ana": 9.5, "Luis": 5.8, "Marta": 8.2, "Pedro": 4.0, "Juan": 9.0}) =>
    {'Aprob': ['Marta'], 'Susp': ['Luis', 'Pedro'], 'Sob': ['Ana', 'Juan']}
    """
    res = {"Aprob": [], "Susp": [], "Sob": []}
    for nombre, nota in estudiantes.items():
        if nota < 6.0:
            res["Susp"].append(nombre)
        elif nota < 9.0:
            res["Aprob"].append(nombre)
        else:
            res["Sob"].append(nombre)
    return res


assert clasificar({"Ana": 9.5, "Luis": 5.8, "Marta": 8.2, "Pedro": 4.0, "Juan": 9.0}) == \
    {'Aprob': ['Marta'], 'Susp': ['Luis', 'Pedro'], 'Sob': ['Ana', 'Juan']}


def cuadrado(n: int) -> list[list[int]]:
    """
    cuadrado(3) => [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    cuadrado(4) => [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]

    fila = list(range(1, n + 1))
    res = []
    for _ in range(n):
        res.append(fila)
        fila = [fila[-1]] + fila[:-1]
    return res
    """
    primera = list(range(1, n + 1))
    return [primera[i:] + primera[:i] for i in range(n, 0, -1)]


assert cuadrado(3) == [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
assert cuadrado(4) == [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]


def es_consecutiva(secuencia) -> bool:
    """
    es_consecutiva([4, 5, 6, 7]) => True
    es_consecutiva([4, 6, 7]) => False
    """
    return secuencia == list(range(min(secuencia), max(secuencia) + 1))


assert es_consecutiva([4, 5, 6, 7]) == True
assert es_consecutiva([4, 6, 7]) == False

from itertools import combinations

def suma(iterable, total: int) -> list[int]:
    """
    suma([1, 2, 3], 5) => [2, 3]
    suma([1, 2, 3], 6) => [1, 2, 3]
    suma([2, 4, 6, 8], 12) => [4, 8] (podría haber sido [2, 4, 6], pero ésta tiene más números)
    suma([4, 10, 8], 24) => []
    """
    lista = sorted(iterable)
    for i in range(1, len(lista) + 1):
        for comb in combinations(lista, i):
            if sum(comb) == total:
                return list(comb)
    return []


assert suma([1, 2, 3], 5) == [2, 3]
assert suma([1, 2, 3], 6) == [1, 2, 3]
assert suma([2, 4, 6, 8], 12) == [4, 8] # (podría haber sido [2, 4, 6], pero ésta tiene más números)
assert suma([4, 10, 8], 24) == []


def contar_elementos(diccionario: dict) -> int:
    """
    contar_elementos({"a": 1, "b": {"c": 2, "d": {"e": 3}}}) => 5
    contar_elementos({"a": 1, "b": {"c": 2}, "d": {"e": 3}}) => 5
    contar_elementos({"a": 1, "b": 8, "c": 2, "d": 6}) => 4
    """
    suma = len(diccionario)
    if suma == 0:
        return 0
    suma += sum(contar_elementos(v) for v in diccionario.values() if type(v) == dict)
    return suma


assert contar_elementos({"a": 1, "b": {"c": 2, "d": {"e": 3}}}) == 5
assert contar_elementos({"a": 1, "b": {"c": 2}, "d": {"e": 3}}) == 5
assert contar_elementos({"a": 1, "b": 8, "c": 2, "d": 6}) == 4


def secuencia_consecutiva(lst1: list[int], lst2: list[int]) -> bool:
    """
    secuencia_consecutiva([1, 4, 5, 7], [2, 3, 6]) => True
    secuencia_consecutiva([1, 4, 5, 6], [2, 7, 8, 9]) => False
    secuencia_consecutiva([1, 4, 5, 6], [2, 3, 7, 8, 10]) => False
    """
    if len(lst1) == 0:
        return lst2 == list(range(min(lst2), max(lst2) + 1))
    return secuencia_consecutiva(lst1[1:], sorted([lst1[0]] + lst2))

    
assert secuencia_consecutiva([1, 4, 5, 7], [2, 3, 6]) == True
assert secuencia_consecutiva([1, 4, 5, 6], [2, 7, 8, 9]) == False
assert secuencia_consecutiva([1, 4, 5, 6], [2, 3, 7, 8, 10]) == False

from math import gcd

def sumar_fracc(tpl1: tuple[int,int], tpl2: tuple[int,int]) -> tuple[int,int]:
    """
    sumar_fracc((1, 6), (1, 3)) => (1, 2) (porque 1/6 + 1/3 = 1/2, una vez simplificada.)
    sumar_fracc((4, 2), (5, 1)) => (7, 1) (porque 4/2 + 5/1 = 7/1, una vez simplificada.)
    """
    n1, d1 = tpl1
    n2, d2 = tpl2
    nr = n1 * d2 + n2 * d1
    dr = d1 * d2
    mcd = gcd(nr, dr)
    return (nr // mcd, dr // mcd)


assert sumar_fracc((1, 6), (1, 3)) == (1, 2) # (porque 1/6 + 1/3 = 1/2, una vez simplificada.)
assert sumar_fracc((4, 2), (5, 1)) == (7, 1) # (porque 4/2 + 5/1 = 7/1, una vez simplificada.)
