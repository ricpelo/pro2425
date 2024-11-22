# EJERCICIO 10.
# Escribir un programa que reciba tres datos de entrada y que los ordene de menor a
# mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

a = 5
b = 2
c = 4

primero = min(a, b, c)
tercero = max(a, b, c)

segundo = a if primero < a and a < tercero else \
          b if primero < b and b < tercero else \
          c
