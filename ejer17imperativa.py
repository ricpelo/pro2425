"""
17. Escribir un programa que calcule la media de cinco valores numéricos reales
(tipo float) introducidos por teclado.
"""

CANTIDAD = 5


def obtener_numero_real():
    while True:
        try:
            n = float(input("Introduzca un número real: "))
            break
        except ValueError:
            print("Valor incorrecto. Vuelva a intentarlo.")
    return n


lista = []
while len(lista) < CANTIDAD:
    n = obtener_numero_real()
    lista.append(n)
media = sum(lista) / CANTIDAD
print("La media es", media)
