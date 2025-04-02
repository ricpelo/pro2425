"""
Ejemplo de manejo de archivos.
"""

import sys

with open("entrada.txt", "r") as f:
    contenido = f.readlines()

# contenido = [linea.strip() for linea in contenido]

for linea in contenido:
    print(linea, end='')

for i, e in enumerate(contenido):
    contenido[i] = 'hola ' + e

with open("entrada.txt", "w") as f:
    f.writelines(contenido)
