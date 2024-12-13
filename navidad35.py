"""
Codificar el juego «el número secreto», que consiste en acertar
un número entre 1 y 100 (generado automáticamente). Para ello se
introduce por teclado una serie de números, para los que se
indica: «mayor» o «menor», según sea mayor o menor con respecto
al número secreto. El proceso termina cuando el usuario acierta
o cuando se rinde (introduciendo un -1).
"""

from random import randrange

secreto = randrange(1, 101)
num_intentos = 1

while True:
    try:
        intento = int(input(f"Introduzca un número (-1 para salir, intento nº {num_intentos}): "))
        if intento == -1:
            break
        if intento == secreto:
            print("¡ENHORABUENA!")
            break
        if intento < secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")
        num_intentos += 1
    except ValueError:
        print("El dato introducido no es un número.")
