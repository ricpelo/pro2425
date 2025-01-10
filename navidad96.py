"""
96. Escribir la función:
suma(lista: list[int], num_elem: int) -> list[int]
que crea y devuelve una lista con las sumas de los num_elem
elementos consecutivos de lista.
Por ejemplo, sea lista = [10, 1, 5, 8, 9, 2]. Si los elementos
de lista se agrupan de 3 en 3, se harán las sumas:
• 10 + 1 + 5 = 16.
• 1 + 5 + 8 = 14.
• 5 + 8 + 9 = 22.
• 8 + 9 + 2 = 19.
Por lo tanto, la función devolverá la lista [16, 14, 22, 19].
"""

def suma(lista: list[int], num_elem: int) -> list[int]:
    """
    Devuelve una lista con las sumas de los num_elem
    elementos consecutivos de la lista.
    """
    res = []
    for i in range(0, len(lista) + 1 - num_elem):
        res.append(sum(lista[i:i+num_elem]))
    return res

print(suma([10, 1, 5, 8, 9, 2], 3))
