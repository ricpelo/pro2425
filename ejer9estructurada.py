"""
9. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
desde el último elemento hasta el primero.
"""

lista = []
while len(lista) < 10:
    cadena = input("Introduzca una cadena: ")
    lista.append(cadena)

i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -= 1

"""
i = -1
while i >= -len(lista):
    print(lista[i])
    i -= 1
"""
