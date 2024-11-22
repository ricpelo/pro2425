"""
Algunas funciones recursivas.
"""

sumatorio = lambda n: 0 if n == 0 else n + sumatorio(n- 1)

potencia = lambda a, b: 1 if b == 0 else a * potencia(a, b - 1)

longitud = lambda s: 0 if s == '' else 1 + longitud(s[1:])

repite = lambda s, n: '' if n == 0 else s + repite(s, n - 1)

suma = lambda i, j: 0 if i > j else i + suma(i + 1, j)
