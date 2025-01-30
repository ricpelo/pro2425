"""
El módulo principal del juego Vampiro.
"""

import mapa as m
import vocabulario as v
from jugador import Jugador

jugador = Jugador(m.vestibulo)
jugador.lugar().describir()

while True:
    entrada = input("¿Qué haces ahora?\n> ")

    # Decodificar la entrada del jugador:
    palabras = entrada.split()
    if len(palabras) == 0:
        continue
    elif len(palabras) > 2:
        print("No entiendo lo que dices.")
        continue
    verbo = v.Palabra.vocabulario.buscar(palabras[0])
    if verbo is None or verbo.categoria() != v.cat_verbo:
        print("No entiendo lo que dices.")
        continue
    if len(palabras) == 2:
        nombre = v.Palabra.vocabulario.buscar(palabras[1])
        if nombre is not None and nombre.categoria() != v.cat_nombre:
            print("No entiendo lo que dices.")
            continue

    # Responder al jugador:
    if verbo == v.fin:
        print("Adiós")
        break
    elif verbo in [v.norte, v.sur, v.este, v.oeste]:
        jugador.intentar_mover(verbo)
