"""
Implementación recursiva de la función factorial
"""

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
resultado = factorial(1000)
print(resultado)