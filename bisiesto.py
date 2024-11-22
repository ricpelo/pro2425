"""
Escribir un programa que pida al usuario un número que representa un año
y determine si ese año es bisiesto o no.
"""

"""
if (anyo % 4 == 0 and anyo % 100 != 0) or anyo % 400 == 0:
    ...
"""

"""
if r:
    print("Sí")
else:
    if p and not q:
        print("Sí")
    else:
        print("No")
"""

try:
    anyo = int(input("Introduzca el año: "))
    p = anyo % 4 == 0
    q = anyo % 100 == 0
    r = anyo % 400 == 0

    if (p and not q) or r:
        print("Sí")
    else:
        print("No")
except ValueError:
    print("Error: valor incorrecto.")
