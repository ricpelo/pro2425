"""
11. Escribe un programa que calcule la longitud y el
área de una circunferencia. Para ello, el usuario debe
introducir el radio (que puede contener decimales).
Recordemos:
𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜
𝑎𝑟𝑒𝑎 = 𝜋 · 𝑟𝑎𝑑𝑖𝑜^2
"""

from math import pi

while True:
    try:
        radio = float(input("Introduzca el radio: "))
        break
    except ValueError:
        print("Error: valor incorrecto")

longitud = round(2 * pi * radio, 3)
area = round(pi * radio ** 2, 3)
print("La longitud de la circunferencia es", longitud)
print("El área de la circunferencia es", area)
