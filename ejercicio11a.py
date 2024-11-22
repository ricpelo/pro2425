# EJERCICIO 11:
# Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
# enteros, de dos formas diferentes:
# a) Mediante la función lcm del módulo math.
# b) Aprovechando la siguiente propiedad:
#    𝑎 · 𝑏 = 𝑚𝑐𝑑 (𝑎, 𝑏) · 𝑚𝑐𝑚(𝑎, 𝑏)

from math import lcm

# Datos de entrada:
a = 8
b = 6

# Dato de salida:
mcm = lcm(a, b)

