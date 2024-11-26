"""
Implementación imperativa de la función factorial usando bucles
"""

def factorial(n: int) -> int:
    """Calcula el factorial de un número."""
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res


def factorial_con_for(n: int) -> int:
    """Calcula el factorial de un número."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(5))
print(factorial_con_for(5))