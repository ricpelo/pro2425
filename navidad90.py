"""
Desarrollar el juego «la cámara secreta», que consiste en abrir una cámara
mediante su combinación secreta, que está formada por una combinación de
dígitos del 1 al 5. El jugador especificará cuál es la longitud de la
combinación; a mayor longitud, mayor será la dificultad del juego. La
aplicación genera, de forma aleatoria, una combinación secreta que el usuario
tendrá que acertar. En cada intento se muestra como pista, para cada dígito de
la combinación introducido por el jugador, si es mayor, menor o igual que el
correspondiente en la combinación secreta.
"""

from random import randrange


def obtener_entero(prompt: str) -> int:
    """Pide un número entero al usuario y no para hasta que se lo da."""
    while True:
        try:
            res = int(input(prompt))
            return res
        except ValueError:
            print("Dato incorrecto.")


num_digitos = obtener_entero("Introduzca el número de dígitos de la combinación secreta: ")
secreto = [randrange(1, 6) for _ in range(num_digitos)]

while True:
    intento = obtener_entero(f"Introduzca la combinación ({num_digitos} dígitos): ")
    intento = [int(x) for x in str(intento)]
    if len(intento) != num_digitos:
        print("Número incorrecto de dígitos.")
        continue
    if intento == secreto:
        print("¡ENHORABUENA!")
        break
    # for c in intento:
    #    print(c, end=' ')
    print(" ".join(map(str, intento)))
    pistas = []
    for i, s in zip(intento, secreto):
        if i < s:
            pistas.append("<")
        elif i > s:
            pistas.append(">")
        else:
            pistas.append("=")
    print(" ".join(pistas))
