"""
100. Diseñar el juego «acierta la contraseña». La mecánica del
juego es la siguiente: el primer jugador introduce la contraseña
sin que la vea el segundo jugador; a continuación, el segundo
jugador debe teclear palabras hasta que la acierte. El programa
deberá indicar en cada intento si la palabra introducida es mayor
o menor (alfabéticamente) que la contraseña.
101. Hacer el mismo programa del ejercicio anterior pero con la
siguiente variante: en lugar de indicar si la palabra es mayor o
menor que la contraseña, deberá mostrar la longitud de la
contraseña y una cadena con los caracteres acertados en sus
lugares respectivos y asteriscos en los no acertados.
"""

password = input("Introduzca la contraseña: ")

while True:
    intento = input("Introduzca la palabra: ")
    for i, e in enumerate(password):
        if i >= len(intento) or intento[i] != e:  # no coincide
            print("*", end='')
        else:                                     # coincide
            print(e, end='')
    print()
    if intento == password:  # acertó
        print("¡Acertó!")
        break
