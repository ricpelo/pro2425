"""
Módulo principal.
"""

from racionales import *

rac1 = racional(2, 3)
rac2 = racional(4, 6)
mult = mult_rac(rac1, rac2)

num = numerador(mult)
den = denominador(mult)

print(f"{num}/{den}")


# suma = racionales.suma_rac(rac1, rac2)
# num, den = suma
# print(f"{num}/{den}")
