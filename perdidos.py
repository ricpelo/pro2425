"""
suma_numeros_perdidos([4, 3, 8, 1, 2]) == 18 # 5 + 6 + 7 = 18
suma_numeros_perdidos([17, 16, 15, 10, 11, 12]) == 27 # 13 + 14 = 27
suma_numeros_perdidos([1, 2, 3, 4, 5]) == 0 # No falta ningún número en la lista
Tests:
suma_numeros_perdidos([1, 2, 3, 4, 5]) == 0
suma_numeros_perdidos([-1, -4, -3, -2, -6, -8]) == -12
"""

def suma_numeros_perdidos(lista: list[int]) -> int:
    """Suma los números perdidos de la lista."""
    """
    return sum(set(range(min(lista), max(lista) + 1)) - set(lista))
    """
    return sum(x for x in range(min(lista), max(lista) + 1) if x not in lista)

    """
    suma = 0
    for x in range(min(lista), max(lista) + 1):
        if x not in lista:
            suma += x
    return suma
    """

assert suma_numeros_perdidos([4, 3, 8, 1, 2]) == 18
assert suma_numeros_perdidos([17, 16, 15, 10, 11, 12]) == 27
assert suma_numeros_perdidos([1, 2, 3, 4, 5]) == 0
assert suma_numeros_perdidos([-1, -4, -3, -2, -6, -8]) == -12


"""
suma_pares_impares([1, 2, 3, 4, 5, 6]) == [12, 9]
suma_pares_impares([-1, -2, -3, -4, -5, -6]) == [-12, -9]
suma_pares_impares([0, 0]) == [0, 0]
suma_pares_impares([]) == [0, 0]
suma_pares_impares([4, 1, 5, 3, 0, 6]) == [10, 9]
suma_pares_impares([0]) == [0, 0]
"""

def suma_pares_impares(lista: list[int]) -> list[int]:
    """Suma los pares y los impares por separado."""
    pares, impares = 0, 0
    for x in lista:
        if x % 2 == 0:
            pares += x
        else:
            impares += x
    return [pares, impares]
    
    """
    pares = sum(x for x in lista if x % 2 == 0)
    impares = sum(x for x in lista if x % 2 != 0)
    return [pares, impares]
    """

assert suma_pares_impares([1, 2, 3, 4, 5, 6]) == [12, 9]
assert suma_pares_impares([-1, -2, -3, -4, -5, -6]) == [-12, -9]
assert suma_pares_impares([0, 0]) == [0, 0]
assert suma_pares_impares([]) == [0, 0]
assert suma_pares_impares([4, 1, 5, 3, 0, 6]) == [10, 9]
assert suma_pares_impares([0]) == [0, 0]


def particion(lista: list[int]) -> int:
    """Divide la lista en dos que suman igual."""
    for i in range(1, len(lista)):
        if sum(lista[:i]) == sum(lista[i:]):
            print(lista[:i], lista[i:])
            return i
    return None



assert particion([10, 20, 30, 5, 40, 50, 40, 15]) == 5 # 10 + 20 + 30 + 5 + 40 = 50 + 40 + 15
assert particion([1, 2, 3, 4, 5, 5]) == 4 # 1 + 2 + 3 + 4 = 5 + 5
assert particion([3, 3]) == 1 # 3 = 3
assert particion([1, 3, 5]) == None
assert particion([3, 4]) == None